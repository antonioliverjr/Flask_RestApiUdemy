from decouple import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


ENGINE = create_engine(config('ENGINE'), convert_unicode=True)
__Metadata=MetaData(schema='hotel') #Somente para demais DB, parametro do declarative_base
__Base = declarative_base()
Session = scoped_session(sessionmaker(autocommit=False, bind=ENGINE))
__Base.query = Session.query_property()

Base = __Base

class Context:
    def __init__(self) -> None:
        self.session = Session
    '''
    Criação única de base de dados, alembic realizando as criações e atualizações
    @staticmethod
    def init_database():
        Base.metadata.create_all(bind=ENGINE)
    '''

    def save(self):
        self.session.commit()
        self.session.close()
    
    def rollback(self):
        self.session.rollback()
