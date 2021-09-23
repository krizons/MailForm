import asyncio
from asyncio import Task
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from conf import settings
from database import db, mail_task
import aiosmtplib
import aiofiles
import traceback
import os.path
import aiofiles.os


class Sender():
    obj_task: Task

    def __init__(self) -> object:
        self.e_stop = asyncio.Event()

    async def sender(self):
        print("START SENDER")

        smtp = aiosmtplib.SMTP(hostname=settings.SMTP_HOST,
                               port=settings.SMTP_PORT,
                               timeout=3,
                               username=settings.SMTP_LOGIN,
                               password=settings.SMTP_PASS,
                               use_tls=True
                               )

        message = MIMEMultipart()
        while not self.e_stop.is_set():
            if not smtp.is_connected:
                try:
                    await smtp.connect()
                    print("CONNECT OK")
                except:
                    print("NOT CONNECT")
                    pass
            else:
                try:
                    async with db.begin() as conn:
                        val = await conn.execute(mail_task.update().returning(*mail_task.c).
                                                 where(mail_task.c.status == "idle").
                                                 values(status="busy"))

                        for msg in val:
                            print(msg)
                            message["From"] = settings.SMTP_LOGIN
                            message["To"] = settings.SEND_MAIL
                            message["Subject"] = ""
                            message.attach(
                                MIMEText("heading:{}\n\rsubtitle:{}\n\rdescription:{}\n\r".format(msg["heading"],
                                                                                                  msg["subtitle"],
                                                                                                  msg["description"])))
                            path_file = msg["path_doc"]
                            print(path_file)
                            if os.path.isfile(path_file):
                                print("File ok")
                                async with aiofiles.open(path_file, 'rb') as doc_file:
                                    part = MIMEApplication(
                                        await doc_file.read(),
                                        Name=os.path.basename(path_file)
                                    )
                                    part['Content-Disposition'] = 'attachment; filename="{0}"'.format(
                                        os.path.basename(path_file))
                                    message.attach(part)
                            try:
                                await smtp.sendmail(settings.SMTP_LOGIN,
                                                    settings.SEND_MAIL,
                                                    message.as_string())
                                await conn.execute(mail_task.delete().where(mail_task.c.id == msg["id"]))
                                if os.path.isfile(path_file):
                                    await aiofiles.os.remove(path_file)
                                print("SEND OK")
                            except:
                                await conn.execute(mail_task.update().
                                                   where(mail_task.c.id == msg["id"]).
                                                   values(status="idle"))
                                print(traceback.format_exc())
                                await asyncio.sleep(5)
                except:
                    print(traceback.format_exc())
            await asyncio.sleep(1)
        if not smtp.is_connected:
            smtp.close()

        print("end")

    async def close(self):
        self.e_stop.set()
# event_loop = asyncio.get_event_loop()
# event_loop.run_until_complete(sender())
# event_loop.close()
