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
from models.engine.file_storage import FileStorage


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
        ''' Create a new instance of a class'''
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

    def emptyline(self):
        '''Nothing happens when there is a blank line'''
        pass

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in d_classes and cnd[0]:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_count(self, cls_name):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count = count + 1
        print(count)

    def do_all(self, line):
        """Prints all data instances, filtered by class (optional)"""

        objList = []
        storage = FileStorage()
        storage.reload()
        objs = storage.all()

        try:
            if len(line) != 0:
                eval(line)

        except NameError:
            print("** class doesn't exist **")
            return

        for _, value in objs.items():
            if len(line) != 0:
                if type(value) is eval(line):
                    objList.append(value)
            else:
                objList.append(value)
        for i in objList:
            print(i)

if __name__ == '__main__':
    '''Console loop'''
    HBNBCommand().cmdloop()
