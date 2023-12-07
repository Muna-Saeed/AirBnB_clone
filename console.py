#!/usr/bin/env python3
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
    prompt = "(hbnb) "

    def emptyline(self):
        """Called when an empty line is entered."""

    def do_help(self, arg):
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
        if not (sys.stdin.isatty()):
            print()
        super().default(line)
    def do_User(self, args):
        eval(f"User{args}")

    def do_Review(self, args):
        eval(f"Review{args}")

    def do_City(self, args):
        eval(f"City{args}")

    def do_Amenity(self, args):
        eval(f"Amenity{args}")

    def do_State(self, args):
        eval(f"State{args}")

    def do_BaseModel(self, args):
        eval(f"BaseModel{args}")
    
    def do_Place(self, args):
        eval(f"Place{args}")


    def count(self, name):
        all = storage.all()
        count = 0
        for key in all.keys():
            sp = key.split(".")
            if sp[0] == name:
                count += 1
        print(count)
    def parser(self, st):
        one = st.split(".")[1]
        d = one.split("(")[1].split(")")[0]
        arg = one.split("(")[0]
        return (arg, d)
        
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
