#!/usr/bin/python3
'''file storage module'''

import json


class FileStorage:
    '''serializes instances to a JSON file and deserializes
    JSON file to instances'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets __objects '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''serializes __ojects to json file'''
        json_obj = {}
        for key, value in self.__objects.items():
            json_obj[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_obj, f)

    def reload(self):
        '''deserializes the json file to __objects'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }

        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
