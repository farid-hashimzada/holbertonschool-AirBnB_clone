#!/usr/bin/python3
"""FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        ser_object = {}
        for key, obj in self.__objects.items():
            ser_object[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(ser_object, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                des_object = json.load(file)
            for key, value in des_object.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            pass
