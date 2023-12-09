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
        if not sys.stdin.isatty():
            print()

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
        if not (sys.stdin.isatty()):
            print()
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
        """ destroy obj """
        if not (sys.stdin.isatty()):
            print()
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

    def do_User(self, args):
        """ User.x() """
        self.manage("User", args)

    def do_Review(self, args):
        """ Review.x() """
        self.manage("Review", args)

    def do_City(self, args):
        """ City.x() """
        self.manage("City", args)

    def do_Amenity(self, args):
        """ Amenity.x() """
        self.manage("Amenity", args)

    def do_State(self, args):
        """ State """
        self.manage("State", args)

    def do_BaseModel(self, args):
        """ BaseModel """
        self.manage("BaseModel", args)

    def do_Place(self, args):
        """ place """
        self.manage("Place", args)

    def count(self, name):
        """ counts objecets """
        all = storage.all()
        count = 0
        for key in all.keys():
            sp = key.split(".")
            if sp[0] == name:
                count += 1
        print(count)

    def manage(self, st, args):
        if not (sys.stdin.isatty()):
            print()
        try:
            if args:
                eval(f"{st}{args}")
            else:
                print(" ** attribute missing **")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
