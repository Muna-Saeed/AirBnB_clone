#!/usr/bin/env python3
""" console.py """
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ main console """
    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered."""

    def do_help(self, arg):
        """ help command """

        if len(arg) == 0:
            if not (sys.stdin.isatty()):
                print()
            print("\nDocumented commands (type help <topic>):")
            print("=" * 40)
            print("EOF  help  quit")
            return
        super().do_help(arg)

    def do_quit(self, arg):
        """ Exit the console."""

        return True

    def do_EOF(self, arg):
        """ Exit on Ctrl-D """

        print()
        return True

    def postcmd(self, stop, line):
        """Called after a command is executed."""
        return stop

    def do_create(self, arg):
        """ create new object """
        if not arg:
            print("** class name missing **")
            return
        if arg in globals():
            obj = globals()[arg]()
            print(obj.id)
            obj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ shows the object """

        if not (sys.stdin.isatty()):
            print()
        if not args:
            print("** class name missing **")
            return
        ls = args.split()
        if (len(ls) > 1):
            obj = self.get_obj(ls)
            if (obj):
                print(obj)
            return
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """ display all """
        if not arg:
            arr = []
            all = storage.all()
            for obj_id in all.keys():
                obj = all[obj_id]
                arr.append(str(obj))
            print(arr)
            return
        ls = []
        if arg in globals():
            arr = []
            all = storage.all()
            for key in all.keys():
                sp = key.split(".")
                obj = self.get_obj(sp)
                if (sp[0] == arg) and obj.__class__.__name__ == arg:
                    arr.append(str(obj))
            print(arr)
            return
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return
        ls = args.split()
        if (len(ls) > 1):
            obj = self.get_obj(ls)
            if (obj):
                storage.destroy_object(obj)
            return
        else:
            print("** instance id missing **")

    def get_obj(self, ls):
        """ gets an object """
        if ls[0] in globals():
            all = storage.all()
            for key in all.keys():
                sp = key.split(".")
                if (sp[1] == ls[1]) and sp[0] == ls[0]:
                    return all[key]
            print("**no instance found **")
            return
        print("** class doesn't exist **")
        return False

    def do_update(self, arg):
        """ update """
        if arg:
            args = arg.split()
            ln = len(args)
            if args[0] in globals():
                if ln == 1:
                    print("** instance id missing *")
                elif ln == 2:
                    print(" ** attribute name missing **")
                elif ln == 3:
                    print(" ** value missing **")
                    return
                else:
                    obj = self.get_obj(args)
                    if obj:
                        storage.set_attr(obj, args[2], args[3])
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def default(self, line):
        """ override default """
        if not (sys.stdin.isatty()):
            print()
        super().default(line)

    def do_User(self, args):
        """ User.x() """
        try:
            eval(f"User{args}")
        except Exception as e:
            print(e)

    def do_Review(self, args):
        """ Review.x() """
        try:
            eval(f"Review{args}")
        except Exception as e:
            print(e)

    def do_City(self, args):
        """ City.x() """
        try:
            eval(f"City{args}")
        except Exception as e:
            print(e)

    def do_Amenity(self, args):
        """ Amenity.x() """
        try:
            eval(f"Amenity{args}")
        except Exception as e:
            print(e)

    def do_State(self, args):
        """ State """
        try:
            eval(f"State{args}")
        except Exception as e:
            print(e)

    def do_BaseModel(self, args):
        """ BaseModel """
        try:
            eval(f"BaseModel{args}")
        except Exception as e:
            print(e)

    def do_Place(self, args):
        """ place """
        try:
            eval(f"Place{args}")
        except Exception as e:
            print(e)

    def count(self, name):
        """ counts objecets """
        all = storage.all()
        count = 0
        for key in all.keys():
            sp = key.split(".")
            if sp[0] == name:
                count += 1
        print(count)

    def parser(self, st):
        """ split """
        one = st.split(".")[1]
        d = one.split("(")[1].split(")")[0]
        arg = one.split("(")[0]
        return (arg, d)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
