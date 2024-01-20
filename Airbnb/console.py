#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of
the command interpreter
"""
from models.base_model import BaseModel
from models import storage
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    prompt command
    """
    prompt = "(hbnb) "

    list_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                    "City": City, "Amenity": Amenity, "Place": Place,
                    "Review": Review}

    def do_quit(self, args):
        """
        Quit the command interpreter
        """
        return True

    def do_EOF(self, args):
        """
        End the command interpreter
        """
        return True

    def emptyline(self):
        """
        Empty the line of the command interpreter
        """
        return False

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if args == "":
            print("** class name missing **")
        elif args not in self.list_classes:
            print("** class doesn't exist **")

        else:
            new_instance = self.list_classes[args]()
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        if args == "":
            print("** class name missing **")
        elif args.split(" ")[0] not in self.list_classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id. (save the change
        into the JSON file).
        """
        if args == "":
            print("** class name missing **")
        elif args.split(" ")[0] not in self.list_classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on
        the class name
        """
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args not in self.list_classes:
            print("** class doesn't exist **")
        else:
            print([str(values) for i, values in storage.all().items()
                  if args in i])
            # print("{}".format(self.list_classes))

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        if args == "":
            print("** class name missing **")
        elif args.split(" ")[0] not in self.list_classes:
            print("** class doesn't exist **")
        elif len(args.split(" ")) < 2:
            print("** instance id missing **")
        elif len(args.split(" ")) < 3:
            print("** attribute name missing **")
        elif len(args.split(" ")) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args.split(" ")[0], args.split(" ")[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                update_obj = args.split()[2]
                value = args.split()[3]
                setattr(storage.all()[key], update_obj, value)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
