from typing import Generator

import sqlalchemy
from sqlalchemy import Column, TEXT, Table
from sqlalchemy import MetaData, inspect
from sqlalchemy.orm import scoped_session, sessionmaker, Session

DATABASE_URL = "sqlite:///data/urls.db"
db_engine = sqlalchemy.create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=db_engine))

if not inspect(db_engine).has_table("url"):
    metadata = MetaData()

    Table(
        "url",
        metadata,
        Column("shorted_url", TEXT(20), primary_key=True),
        Column("target_url", TEXT, nullable=False),
    )

    metadata.create_all(bind=db_engine)


def get_db_session() -> Generator[Session, None, None]:
    db = db_session()

    try:
        yield db
    finally:
        db.close()
