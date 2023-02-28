#!/usr/bin/python3


from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from model_state import Base, State


class City(Base):
    """ City class """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=True)
