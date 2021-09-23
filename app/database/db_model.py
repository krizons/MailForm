import sqlalchemy

metadata = sqlalchemy.MetaData()
mail_task = sqlalchemy.Table(
    "mail_task",
    metadata,
    sqlalchemy.Column("heading", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("subtitle", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("description", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("path_doc", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("status", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True),
    )
