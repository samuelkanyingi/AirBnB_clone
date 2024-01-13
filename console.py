#!/usr/bin/python3

import cmd
import sys
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    """simple command interpreter"""
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        """exit using EOF"""
        return True
    def emptyline(self):
        """do nothing on empty line"""
        pass
    def run_it(self, input_stream):
        for line in input_stream:
            self.onecmd(line.strip())
    def do_create(self, arg):
        if not arg:
            print("**class name missing **")
            return
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """prints string representation of instance"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
            return
        if args[0]  not in self.valid_classes:
            print("** class does not exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        key = args[1]
        all_instances = BaseModel.all()
        #print("Key to find:", key)
        #print("Type of key:", type(key))
        #print("All Keys in all_instances:", list(all_instances.keys()))
        #print("All Instances:", all_instances)
         
        if key not in all_instances:
            print("**no instance found **")
            return
        instance = all_instances[key]
        print(str(instance))
        #print("Instance found:", all_instances[key])
    def do_destroy(self, arg):
        """deletes an instance"""
        args = arg.split()
        if not args:
            print("** class name is missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(arg[0], arg[1])
        all_instances = BaseModel.all()
        if key not in all_instances:
            print("** no instance found **")
            return
        del all_instances[key]
        BaseModel.save_to_file(all_instances)

    def do_all(self, arg):
        """prints string representation of instances"""
        args = arg.split()
        all_instances = BaseModel.all() 

        if not args:
            print([str(obj) for obj in all_instances.values()])
        elif args[0] in self.valid_classes:
            #class_key = f"{args[0]}."
            #print("empty")
            result=[str(obj) for obj in all_instances.values()if type(obj).__name__ == args[0]]
            #result = [str(obj) for key, obj in all_instances.items() if key.startswith(class_key)]
            print(result)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        #print("Class name:", args[0])
        #print("Instance ID:", args[1])
        #print("All Instance Keys:", BaseModel.all().keys())
        if "{}.{}".format(args[0], args[1]) not in BaseModel.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        instance = BaseModel.all()[key]
        attr_name = args[2]
        attr_value = args[3]
        self.base_model_instance.update_instance(arg[1], attribute, value)

#        if hasattr(instance, attr_name):
 #           attr_type = type(getattr(instance, attr_name))
  #          try:
   #             converted_value = attr_type(attr_value)
    #            setattr(instance, attr_name, converted_value)
     #           instance.save()
      #      except ValueError:
       #         print("** invalid attribute value type **")
        #else:
         #   print("** attribute not found **")


if __name__ == '__main__':
    my_loop=HBNBCommand()
    if not sys.stdin.isatty():
        my_loop.run_it(sys.stdin)

    else:
        my_loop.cmdloop()
