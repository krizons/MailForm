import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from conf import settings
from database import db, mail_task
import aiosmtplib
import aiofiles

import os.path


async def sender():
    #print("START SENDER")
    await  db.connect()
    smtp = aiosmtplib.SMTP(hostname=settings.SMTP_HOST,
                           port=settings.SMTP_PORT,
                           timeout=3,
                           username=settings.SMTP_LOGIN,
                           password=settings.SMTP_PASS,
                           use_tls=True
                           )

    message = MIMEMultipart()
    while True:
        if not smtp.is_connected:
            try:
                await smtp.connect()
            except:
                print("NOT CONNECT")
                pass
        else:
            val = await db.fetch_all(mail_task.select())
            for msg in val:
                message["From"] = settings.SMTP_LOGIN
                message["To"] = settings.SEND_MAIL
                message["Subject"] = ""
                message.attach(MIMEText("heading:{}\n\rsubtitle:{}\n\rdescription:{}\n\r".format(msg.get("heading"),
                                                                                                 msg.get("subtitle"),
                                                                                                 msg.get(
                                                                                                     "description"))))
                path_file = msg.get("path_doc")
                if os.path.isfile(path_file):
                    async with aiofiles.open(path_file, 'rb') as doc_file:

                        part = MIMEApplication(
                            await doc_file.read(),
                            Name=os.path.basename(path_file)
                        )
                        part['Content-Disposition'] = 'attachment; filename="{0}"'.format(os.path.basename(path_file))
                        message.attach(part)
                try:
                    await smtp.sendmail(settings.SMTP_LOGIN,
                                        settings.SEND_MAIL,
                                        message.as_string())

                    await db.execute(mail_task.delete().where(mail_task.c.id == msg.get("id")))
                except:
                    pass

        await asyncio.sleep(3)


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(sender())
