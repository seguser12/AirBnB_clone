#!/usr/bin/python3
'''console module'''

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''entry point of command interpreter'''
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def emptyline(self):
        '''overides the cmd emptyline method to print nothing'''
        pass

    def do_EOF(self, line):
        '''handles EOF to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_create(self, cls_name):
        '''creates a new instance of BaseModel and save to json file'''
        if not cls_name:
            print("** class name missing **")
            return
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        my_model = self.classes[cls_name]()
        my_model.save()
        print(my_model.id)

    def do_show(self, line):
        '''prints str_rep of an instance based on class name and id'''
        if not line:
            print("** class name missing **")
            return

        args = line.split(" ")
        cls_name = args[0]

        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = f'{cls_name}.{id}'
        try:
            new_model = storage.all()
            my_model = new_model[key]
            print(my_model)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        '''deletes an instance based on the class name and id'''
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        cls_name = args[0]
        id = args[1] if len(args) > 1 else None

        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        if not id:
            print("** instance id missing **")
            return
        try:
            key = f'{cls_name}.{id}'
            my_model = storage.all()
            del my_model[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        '''prints all str rep of all instances based or not on the
        class name'''
        my_model = []
        my_models = storage.all()

        if line:
            cls_name = line.split(' ')[0]
            if cls_name not in self.classes:
                print("** class doesn't exist **")
                return
            for key, value in my_models.items():
                if key.split('.')[0] == cls_name:
                    my_model.append(str(value))
        else:
            for key, value in my_models.items():
                my_model.append(str(value))

        print(my_model)

    def do_update(self, line):
        '''updates an instance based on the class name and id'''
        args = line.split(" ")
        cls_name = args[0]
        id = args[1] if len(args) > 1 else None
        attr_name = args[2] if len(args) > 2 else None
        attr_value = args[3] if len(args) > 3 else None

        if not cls_name:
            print("** class name missing **")
            return
        if cls_name not in self.classes:
            print("** class doesn't exist **")
            return
        if not id:
            print("** instance id missing **")
            return

        key = f"{cls_name}.{id}"
        my_models = storage.all()
        if key not in my_models:
            print("**no instance found **")
            return
        if not attr_name:
            print("** attribute name missing **")
            return
        if not attr_value:
            print("** value missing **")
            return
        try:
            my_model = my_models[key]
            my_model.__dict__[attr_name] = eval(attr_value)
            my_model.save()
        except Exception:
            my_model.__dict__[attr_name] = attr_value
            my_model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
