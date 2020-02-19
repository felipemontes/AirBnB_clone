#!/usr/bin/python3
'''HBNBCommand Modules'''
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

d_classes = {'BaseModel': BaseModel, 'User': User,
             'State': State, 'City': City,
             'Amenity': Amenity, 'Place': Place,
             'Review': Review}


class HBNBCommand(cmd.Cmd):
    '''Console'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, arg):
        '''End of file'''
        return True

    def do_create(self, arg):
        '''Creates a new instance of a class'''
        if not arg:
            print("** class name missing **")
        else:
            if arg not in d_classes:
                print("** class doesn't exist **")
            else:
                attr = d_classes[arg]()
                print(attr.id)
                attr.save()

    def do_show(self, arg):
        '''String representation of an instance based on the
           class name and id
        '''
        spl = split(arg)
        if not arg:
            print("** class name missing **")
        elif spl[0] not in d_classes:
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
        '''Deletes an instance based on the class name and id'''
        spl = split(arg)
        if not arg:
            print("** class name missing **")
        elif spl[0] not in d_classes:
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
        '''Prints all string representation of all instances
           based or not on the class name
        '''
        spl = split(arg)
        l_objs = []
        if not arg:
            for v in storage.all().values():
                l_objs.append(v.__str__())
            print(l_objs)
        elif spl[0] not in d_classes:
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if v.__class__ == eval(spl[0]):
                    l_objs.append(v.__str__())
            print(l_objs)

    def do_update(self, arg):
        '''Updates an instance based on the class name
           and id by adding or updating attribute
        '''
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
                print('** attribute name missing **')
            elif len(spl) == 3:
                print('** value missing **')
            else:
                for k, v in storage.all().items():
                    setattr(storage.all()[key], spl[2], spl[3])
                    storage.save()
                return

    def emptyline(self):
        '''Nothing happens when there are blank lines'''
        pass

if __name__ == '__main__':
    '''Console loop'''
    HBNBCommand().cmdloop()
