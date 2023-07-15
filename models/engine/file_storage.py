#!/usr/bin/python3
'''file storage module'''

import json


class FileStorage:
    '''File storage class that serializes instances to a json file'''
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        '''return the dictionary __objects'''
        if cls:
            return {key: val for (key, val) in self.__objects.items()}
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key'''
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to json file'''
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict, f)

    def reload(self):
        '''deserializes the json file'''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for key, value in json.load(f).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
