#!/usr/bin/python3
"""
improve model_city.py and model_state.py
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
import sys


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
