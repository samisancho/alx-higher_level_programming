#!/usr/bin/python3


from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ City class """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=True)
