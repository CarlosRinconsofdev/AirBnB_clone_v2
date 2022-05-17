#!/usr/bin/python3
"""DBStorage for sqlalchemy"""
from os import getenv
from sqlalchemy import create_engine
from models.user import User
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place, place_amenity
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session
from models.review import Review

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Amenity': Amenity,
    'Place': Place,
    'City': City,
    'Review': Review
}

class DBStorage:
    """ Query on the current database session """
    __engine = None
    __session = None
    
    def __init__(self):
        """Initialization of data and ENVs"""
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine(
            f'mysql+mysqldb://{USER}:{PWD}@{HOST}/{DB}', pool_pre_ping=True)
    
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return dictionary of models currently in storage"""
        tdict = {}
        obj_list = []
        classes = [State, City, User, Place, Review, Amenity]
        if cls is not None:
            obj_list = self.__session.query(cls).all()
        else:
            for cls_ in classes:
                obj_list += self.__session.query(cls_).all()
        for obj in obj_list:
            tdict[obj.__class__.__name__ + "." + str(obj.id)] = obj
        return tdict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
