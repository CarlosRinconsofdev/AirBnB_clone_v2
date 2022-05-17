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
        new_dict = {}
        if cls is not None:
            query_cls = self.session.query(cls).all()
            for obj in query_cls:
                key = "{}.{}".format(self.__class__.__name__, obj.id)
                new_dict[key] = obj
        else:
            for value in classes:
                query = self.__session.query(classes[value]).all()
                for obj in query:
                    key = "{}.{}".format(self.__class__.__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ Add the object """
        self.__session.add(obj)

    def save(self):
        """ Commit the database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete  obj if not none """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session)
        self.__session = session()
