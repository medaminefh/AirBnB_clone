#!/usr/bin/python3
"""
This is the entry file of our program
"""

import cmd

class Console(cmd.Cmd):
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
        this will quit the program
        """
        return True
        
    def postloop(self):
        print()
    
if __name__ == "__main__":
    Console().cmdloop()