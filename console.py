#!/usr/bin/python3
'''console module'''

import cmd


class HBNBCommand(cmd.Cmd):
    '''entry point of command interpreter'''
    prompt = '(hbnb) '

    def emptyline(self):
        '''overides the cmd emptyline method to print nothing'''
        pass

    def do_EOF(self, line):
        '''handles EOF to exit program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
