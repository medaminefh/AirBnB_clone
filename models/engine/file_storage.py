#!/usr/bin/python3
'''
file storage engine
'''
import json
import os.path


class FileStorage():
    ''' Represte the FileStorage class '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''  Return the dictionary '''
        return self.__objects

    def new(self, obj):
        '''  sets in __objects the obj with key '''
        key = "<{}>.{}".format(obj.__class__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' '''
        serilizer = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as f:
            return f.write(serilizer)

    def reload(self):
        ''' '''
        if os.path.isfile(__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
