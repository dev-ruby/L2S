from sqlalchemy import Column, TEXT
from sqlalchemy.ext.declarative import declarative_base

from .db import db_engine

base = declarative_base()
base.metadata.create_all(bind=db_engine)


class Url(base):
    __tablename__ = "url"
    shorted_url = Column(TEXT(20), primary_key=True)
    target_url = Column(TEXT, nullable=False)
