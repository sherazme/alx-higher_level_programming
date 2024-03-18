#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
"""
creates States class based on Base
"""

Base = declarative_base()


class State(Base):
    """
	inheritance from Base class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
