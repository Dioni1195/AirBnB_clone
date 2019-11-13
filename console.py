#!/usr/bin/python3
"""This is the console for the Holberton HNBN project
    Authors: Dionisio Arango & Juan Calle
"""
# =========================================================
# ||        ██╗  ██╗██████╗ ███╗   ██╗██████╗            ||
# ||        ██║  ██║██╔══██╗████╗  ██║██╔══██╗           ||
# ||        ███████║██████╔╝██╔██╗ ██║██████╔╝           ||
# ||        ██╔══██║██╔══██╗██║╚██╗██║██╔══██╗           ||
# ||        ██║  ██║██████╔╝██║ ╚████║██████╔╝           ||
# =========================================================


import cmd

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


def error_msg(n):
    """Function  that returns error messages
        - n: as argument identifier for error msg
    """
    msg_dict = {1: "** class name missing **",
                2: "** class doesn't exist **",
                3: "** instance id missing **",
                4: "** no instance found **",
                5: "** attribute name missing **",
                6: "** value missing **"
                }
    for key, item in msg_dict.items():
        if key == n:
            print(item)


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt
       prompt - The start prompt for the Daionisio console

    """
    prompt = "(hbnb) "

    class_set = {'BaseModel',
                 'User',
                 'State',
                 'City',
                 'Amenity',
                 'Place',
                 'Review'}

    def do_create(self, arg):
        """Function that creates a new instance of BaseModel and saves
        the instance to a JSON file"""

        if arg == "":
            error_msg(1)
        elif arg not in self.class_set:
            error_msg(2)
        else:
            arg = eval(arg)()
            arg.save()
            print(arg.id)

    def do_show(self, line):
        """Function to print string representation of instance"""
        arg = line.split()
        if line == "":
            error_msg(1)
        elif arg[0] not in self.class_set:
            error_msg(2)
        elif len(arg) < 2:
            error_msg(3)
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            try:
                obj = data_dump[key]
                print(obj)
            except KeyError:  # is this repeated?
                error_msg(4)

    def do_destroy(self, line):
        """Function that prints string representation of instance"""
        arg = line.split()  # Is this the trouble?
        if line == "":
            error_msg(1)
        elif arg[0] not in self.class_set:
            error_msg(2)
        elif len(arg) < 2:
            error_msg(3)
        else:
            data_dump = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump.keys():
                del data_dump[key]
                models.storage._FileStorage__objects = data_dump
                models.storage.save()
                return
            error_msg(4)

    def do_all(self, line=""):
        """Function that displays all class instances of given argument or all
        if no argument given"""
        data_dump = models.storage.all()
        list_print = []
        arg = line.split()
        if line is "":
            for instance_key, instance_obj in data_dump.items():
                list_print.append(str(instance_obj))
            print(list_print)

        else:
            if arg[0] not in self.class_set:
                error_msg(2)
            else:
                for instance_key, instance_obj in data_dump.items():
                    class_key = instance_obj.to_dict()
                    if class_key['__class__'] == arg[0]:
                        list_print.append(str(instance_obj))
                print(list_print)

    def do_update(self, line=""):
        """ Function that Updates an instance based on the class
        name and id by adding or updating attribute and save
        the change into the JSON file"""
        data_dump = models.storage.all()

        arg = line.split()

        if not line:
            error_msg(1)
        elif arg[0] not in self.class_set:
            error_msg(2)
        elif len(arg) < 2:
            error_msg(3)
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in data_dump:
                if len(arg) < 3:
                    error_msg(5)
                elif len(arg) < 4:
                    error_msg(6)
                else:
                    obj = data_dump[key].to_dict()
                    obj.update({arg[2]: arg[3]})
                    new_ins = globals()[arg[0]](**obj)
                    new_ins.save()
            else:
                error_msg(4)

    def default(self, line):
        """ This method is called when the command is not recognized """
        arg = line.split(".")
        if len(arg) > 1:
            if arg[1].find("all") != -1:
                self.do_all(arg[0])
            elif arg[1].find("count") != -1:
                count = 0
                data_dump = models.storage.all()
                for key in data_dump.keys():
                    if key.find(arg[0]) != -1:
                        count += 1
                print(count)
            elif arg[1].find("show") != -1:
                # Here split the show(<id>) to obtain <id>)
                cmmd_split = arg[1].split('(')
                # Here obtain the id without ')'
                id_to_search = cmmd_split[1][:-1]
                self.do_show(str(arg[0]) + ' ' + id_to_search)
            elif arg[1].find("destroy") != -1:
                # Here split the show(<id>) to obtain <id>)
                cmmd_split = arg[1].split('(')
                # Here obtain the id without ')'
                id_to_search = cmmd_split[1][:-1]
                self.do_destroy(str(arg[0]) + ' ' + id_to_search)
            elif arg[1].find("update") != -1:
                cmmd_split = arg[1].split(',', 1)
                print(len(cmmd_split))
                if len(cmmd_split) > 2:
                    id_update = ' ' + cmmd_split[0][7:]
                    attr_name = cmmd_split[1]
                    attr_value = cmmd_split[2]
                    self.do_update(arg[0] + id_update + attr_name + attr_value)
                else:
                    id_update = ' ' + cmmd_split[0][7:]
                    dict_rep = cmmd_split[1]
                    dict_update = dict_rep.split(',')
                    print(dict_update)
                    for pair in dict_update:
                        pair = pair.split(':')
                        print(pair)
                        """#key = ' ' + pair[0][3:-1]
                        #value = ' ' + pair[1][1:-2]
                        #self.do_update(arg[0] + id_update + key + value)"""
        else:
            pass

    def emptyline(self):
        """Called when an empty line is entered
        Prints the prompt again
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on Daionisio console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
