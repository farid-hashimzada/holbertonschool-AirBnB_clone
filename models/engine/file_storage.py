#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """ Add object to objects"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Save objects to file"""
        ser_object = {}
        for key, obj in self.__objects.items():
            ser_object[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_object, file)

     def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                for key, value in json.load(f).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
