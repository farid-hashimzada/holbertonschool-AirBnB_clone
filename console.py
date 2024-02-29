#!/usr/bin/python3
"""Console module"""
import cmd
from models.base_model import BaseModel
from models import storage


class SysConsole(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program"""
        return True

    def do_help(self, arg):
        """Help command"""
        return super().do_help(arg)

    def emptyline(self) -> bool:
        """Empty line"""
        return False

    def do_create(self, arg):
        """Create command"""
        if not arg:
            print("** class name missing **")
        elif arg not in BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Show model with id"""
        lines = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif lines[0] not in BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            key = lines[0] + "." + lines[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy instance"""
        lines = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif lines[0] not in BaseModel.__name__:
            print("** class doesn't exist ** ")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            key = lines[0] + "." + lines[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string repr"""
        if arg not in BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                print(value)


if __name__ == '__main__':
    SysConsole().cmdloop()
