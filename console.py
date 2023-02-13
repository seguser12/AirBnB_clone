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
            print("** no instance found **")
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

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}') + 1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(') + 1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(') + 1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        '''retrieves all instances of a class and number of instances'''
        args = line.split('.')
        if len(args) >= 2:
            cls_name = args[0]
            func = args[1]
            if func == "all()":
                self.do_all(cls_name)
            elif func == "count()":
                counter = 0
                if cls_name not in self.classes:
                    print("** class doesn't exist **")
                obj = storage.all()
                for key in obj:
                    counter += 1
                print(counter)
            elif func[:4] == "show":
                self.do_show(self.strip_clean(args))
            elif func[:7] == "destroy":
                self.do_destroy(self.strip_clean(args))
            elif func[:6] == "update":
                arg_list = self.strip_clean(args)
                if isinstance(arg_list, list):
                    obj = storage.all()
                    key = arg_list[0] + ' ' + arg_list[1]
                    for key, val in arg_list[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(key, val))
                else:
                    self.do_update(arg_list)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
