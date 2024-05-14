from sqlalchemy import column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = column(Integer, primary_key=True)
    name = column(String)