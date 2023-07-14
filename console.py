#!/usr/bin/python3
'''Console module'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''class definition of the entry point of command interpreter'''
    prompt = '(hbnb) '

    def do_EOF(self, line):
        '''eof to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit program'''
        raise SystemExit

    def emptyline(self):
        '''ignores empty line + enter'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
