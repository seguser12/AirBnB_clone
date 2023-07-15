#!/usr/bin/python3
'''Console module'''

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''class definition of the entry point of command interpreter'''
    prompt = '(hbnb) '
    classes = {'BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review'}

    def do_EOF(self, line):
        '''eof to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit program'''
        raise SystemExit

    def emptyline(self):
        '''ignores empty line + enter'''
        pass

    def do_create(self, line):
        '''
        creates instance of class and save it to json
        usage: create <class name>
        '''
        if not line:
            print('** class name missing **')
        else:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, line):
        '''
        prints string rep of an instance base on class name and id
        usage: show <class name> <id>'''
        if not line:
            print('** class name missing **')
        else:
            args = line.split(' ')
            class_name = args[0]
            class_id = args[1] if len(args) > 1 else None
            if class_name not in self.classes:
                print("** class doesn't exist **")
            elif not class_id:
                print("** instance id missing **")
            else:
                key = f"{class_name}.{class_id}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        '''
        deletes an instance based on the class name and id
        usage: destroy <class name> <id>
        '''
        args = line.split(' ')
        class_name = args[0] if len(args) > 0 else None
        class_id = args[1] if len(args) > 1 else None

        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        elif class_id is None:
            print("** instance id missing **")
        else:
            key = f'{class_name}.{class_id}'
            try:
                del storage.all()[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        '''
        prints all string rep. of all instances based on or not class name
        usage: $ all BaseModel or $ all
        '''
        my_list = []
        if line:
            class_name = line.split(' ')[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            objects = storage.all(class_name)
            for key in objects:
                name = key.split('.')[0]
                if name == class_name:
                    my_list.append(str(objects[key]))
            print(my_list)
        else:
            objects = storage.all()
            for key in objects:
                my_list.append(str(objects[key]))
            print(my_list)
            return

    def do_update(self, line):
        '''
        updates an instance based on the class name and id and
        saves the change to json file
        usage: <class name> <id> <attribute name> "<attribute value>"
        '''
        args = line.split(' ')
        class_name = args[0]
        class_id = args[1] if len(args) > 1 else None
        att_name = args[2] if len(args) > 2 else None
        att_value = args[3] if len(args) > 3 else None
        if not line:
            print("** class name missing **")
            return

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        objects = storage.all()
        key = f'{class_name}.{class_id}'
        if key not in objects:
            print("** no instance found **")
            return
        if not att_name:
            print("** attribute name missing **")
            return
        if not att_value:
            print("** value missing **")
            return
        val = objects[key]
        try:
            val.__dict__[att_name] = eval(att_value)
        except Exception as e:
            val.__dict__[att_name] = att_value
            val.save()

    def count(self, line):
        '''count the number of instances of a class'''
        count = 0
        try:
            class_name = line.split(' ')[0]
            if class_name not in self.classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')[0]
                if name == class_name:
                    count += 1
            print(count)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips the argument and return a string of command"""
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """retrieve all instances of a class and
        retrieve the number of instances
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
