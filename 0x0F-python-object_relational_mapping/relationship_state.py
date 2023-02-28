#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """ State class """
    __tablename__ = 'states'

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    cities = relationship("City", backref="state", cascade="all, delete")
