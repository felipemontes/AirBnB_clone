#!/usr/bin/python3
''' FileStorage Modules '''
import json
import os.path


class FileStorage:
    ''' Serializes instances to a JSON file and
    deserializes JSON file to instances '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns a dictionary '''
        return self.__objects

    def new(self, obj):
        ''' Sets the object in the key '''
        k = obj.__class__.__name__ + '.' + obj.id
        self.__objects[k] = obj

    def save(self):
        ''' Serializes __objects to the JSON file '''
        d = {}
        for k, v in self.__objects.items():
            d[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        ''' deserializes the JSON only if the path exist '''
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User,
               'Place': Place, 'State': State,
               'City': City, 'Amenity': Amenity, 'Review': Review}

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for k, v in json.load(f).items():
                    self.new(dct[v['__class__']](**v))
