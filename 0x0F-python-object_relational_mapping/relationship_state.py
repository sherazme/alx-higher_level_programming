#!/usr/bin/python3
'''State model'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
'''Represents base class for tables'''


class State(Base):
    '''Represents row in states table'''
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(length=128),
        nullable=False
    )
    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )
