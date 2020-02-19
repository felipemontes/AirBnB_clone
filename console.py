#!/usr/bin/python3
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
d_classes = {'BaseModel': BaseModel, 'User': User,
               'Place': Place, 'State': State,
               'City': City, 'Amenity': Amenity, 'Review': Review}

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        ''' Quit command to exit the program\n '''
        return True

    def do_EOF(self):
        ''' End of file'''
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return

        for k, v in d_classes.items():
            if arg not in list(d_classes):
                print("** class doesn't exist **")

            else:
                attr = d_classes[arg]()
                print(attr.id)
                attr.save()

    def do_show(self, arg):
        '''Comment'''
        spl = split(arg)
        if not arg:
            print("** class name missing **")
            return
        if spl[0] not in d_classes:
            print("** class doesn't exist **")
        else:
            if len(spl) == 1:
                print('** instance id missing **')
            else:
                key = spl[0] + '.' + spl[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print('** no instance found **')

    def do_destroy(self, arg):
        '''Comment'''
        spl = split(arg)
        if not arg:
            print("** class name missing **")
            return
        if spl[0] not in d_classes:
            print("** class doesn't exist **")
        else:
            if len(spl) == 1:
                print('** instance id missing **')
            else:
                key = spl[0] + '.' + spl[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print('** no instance found **')

    def do_all(self, arg):
        ''' Prints all string representation of all instances '''
        spl = split(arg)
        newlist = []
        if len(spl) == 0 or spl[0] not in d_classes:
            print("** class doesn't exist **")
        else:
            for v in storage.all().values():
                    newlist.append(v.__str__())
            print (newlist)

    def update(self, arg):
        ''' Updates an instance based on the class name and id '''
        spl = split(arg)
        if not arg:
            print("** class name missing **")
        elif spl[0] not in d_classes:
            print("** class doesn't exist **")
        elif len(spl) == 1:
            print('** instance id missing **')
        else:
            key = spl[0] + '.' + spl[1]
            if key not in storage.all():
                print('** no instance found **')
            elif len(spl) == 2:
                print('** value missing **')
            else:
                for k, v in storage.all().items():
                    setattr(storage.all()[key], spl[2], spl[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
