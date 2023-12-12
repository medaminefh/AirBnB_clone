#!/usr/bin/python3
"""
This is the entry file of our program
"""

import cmd
import re
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

    def emptyline(self):
        """ Pass if you hit enter.
        """
        pass

    def do_create(self, line):
        """
        create an instance of the BaseModel
        """
        if not line:
            print("** class name missing **")
            return
        if line not in storage.originalClass():
            print("** class doesn't exist **")
            return

        instance = storage.originalClass()[line]()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        show us the string rep of the class
        """

        commands = line.split()
        all_instances = storage.all()

        if not line:
            print('** class name missing **')
            return
        elif commands[0] not in storage.originalClass():
            print("** class doesn't exist **")
            return
        elif len(commands) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(commands[0], commands[1])
        obj = all_instances.get(key)
        if not obj:
            print("** no instance found **")
            return
        else:
            print(obj)

    def do_destroy(self, line):
        """
        destroy an instance from the file
        """

        commands = line.split()

        if not line:
            print('** class name missing **')
            return
        elif commands[0] not in storage.originalClass():
            print("** class doesn't exist **")
            return
        elif len(commands) < 2:
            print("** instance id missing **")
            return
        else:
            all_instances = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if not all_instances.get(key):
                print("** no instance found **")
                return
            del all_instances[key]
            storage.save()

    def do_all(self, line):
        """
        show all the objects(instances) of the specified Class
        """

        all_instances = storage.all()
        if not line or line == ".":
            list_obj = [str(obj) for _, obj in all_instances.items()]
            print(list_obj)
            return
        else:
            if line not in storage.originalClass():
                print("** class doesn't exist **")
                return
            list_obj = [str(obj) for _, obj in all_instances.items()
                        if type(obj).__name__ == line]
            print(list_obj)

    def do_update(self, line):
        """
        update an instance attr from its name and id
        """
        regex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(regex, line)
        classname = match.group(1)
        class_id = match.group(2)
        attr = match.group(3)
        value = match.group(4)

        if not match:
            print('** class name missing **')
            return
        if classname not in storage.originalClass():
            print("** class doesn't exist **")
            return
        if not class_id:
            print("** instance id missing **")
            return
        all_instances = storage.all()
        key = "{}.{}".format(classname, class_id)
        instance = all_instances.get(key)
        if not instance:
            print("** no instance found **")
            return
        if not attr:
            print("** attribute name missing **")
            return
        if not value:
            print("** value missing **")
            return

        setattr(instance, attr, value.replace('"', ""))
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
