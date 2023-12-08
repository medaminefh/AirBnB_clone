#!/usr/bin/python3
"""
This is the entry file of our program
"""

import cmd
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, line):
        """
        create an instance of the BaseModel
        """
        if not line:
            print("** class name missing **")
            return
        if line != "BaseModel":
            print("** class doesn't exist **")
            return

        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        show us the string rep of the class
        """

        class_name, class_id = line.split()
        all_instances = storage.all()
        key = "<{}>.{}".format(class_name, class_id)

        # TODO: this is not working
        obj = all_instances.get(key).to_dict()
        obj = {key: obj[key] for key in obj if key != "__class__"}

        if not class_name:
            print('** class name missing **')
            return
        elif class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        elif not class_id:
            print("** instance id missing **")
            return
        elif not obj:
            print("** no instance found **")
            return
        else:
            print(obj)

    def do_all(self, line):
        """
        show all the objects(instances) of the specified Class
        """

        all_instances = storage.all()
        if not line:
            print(all_instances)
        else:
            print("filter the instances of", line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
