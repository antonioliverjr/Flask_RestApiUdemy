from __future__ import annotations
#from abc import ABC
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


ENGINE = create_engine('sqlite:///database.db', convert_unicode=True)
__Base = declarative_base()
Session = scoped_session(sessionmaker(autocommit=False, bind=ENGINE))
__Base.query = Session.query_property()

Base = __Base

class Context:
    def __init__(self) -> None:
        self.session = Session

    @staticmethod
    def init_database():
        Base.metadata.create_all(bind=ENGINE)

    def save(self):
        self.session.commit()
        self.session.close()
    
    def rollback(self):
        self.session.rollback()
