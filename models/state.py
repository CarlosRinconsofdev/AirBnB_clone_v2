#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref='state')
    
    @property
    def cities(self):
        """getter for list of city instances related to theate"""
        city_instances = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_instances.append(city)
        return city_instances
