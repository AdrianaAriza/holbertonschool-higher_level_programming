#!/usr/bin/python3
""""""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":

    Base = declarative_base()

    class State(Base):

        __tableame__ = states
        id = Column(Integer, primary_key=True, autoincrement=Ture, nullable=False)
        name = Column(String(128), nullable=False)
