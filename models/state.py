#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')
    @property
    def cities(self):
        """getter for list of city instances related to theate"""
        cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
