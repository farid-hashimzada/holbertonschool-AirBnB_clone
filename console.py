#!/usr/bin/python3
import cmd
"""Console module"""


class SysConsole(cmd.Cmd):
    """Console class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit program"""
        return True

    def do_help(self, arg: str) -> bool | None:
        """Help command  show help message"""
        return super().do_help(arg)

    def emptyline(self) -> bool:
        """Empty line"""
        return False


if __name__ == '__main__':
    SysConsole().cmdloop()
