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

    def delete(self, obj=None):
        """Deletes obj if it's inside the attribute __objects
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if (key, obj) in self.__objects.items():
                self.__objects.pop(key, None)
        self.save()

    def close(self):
        """Deserializes the JSON file to objects"""
        self.reload()

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
