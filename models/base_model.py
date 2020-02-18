#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
T = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    '''BaseModel class'''
    def __init__(self, *args, **kwargs):
        '''Constructor'''
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, T)
                if k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        '''Str method'''
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of
           __dict__ of the instance
        '''
        d = {}
        for k, v in self.__dict__.items():
            if k == 'created_at' or k == 'updated_at':
                d[k] = v.strftime(T)
            else:
                d[k] = v
        d['__class__'] = self.__class__.__name__
        return d
