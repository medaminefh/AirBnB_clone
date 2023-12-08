#!/usr/bin/python3
"""
This is the entry file of our program
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This is the console class of our program (the interpreter)
    """
    prompt = "(hbnb) "

    def do_EOF(self, _):
        """
        this will run if the interpreter is running on mode interactive
        """
        return True

    def do_quit(self, _):
        """
        Quit command to exit the program
        """
        return True

    def postloop(self):
        """
        post loop function
        """
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
