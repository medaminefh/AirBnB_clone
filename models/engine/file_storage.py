#!/usr/bin/python3
'''
file storage engine
'''
import json
import os


class FileStorage():
    ''' Represte the FileStorage class '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''  Return the dictionary '''
        return FileStorage.__objects

    def new(self, obj):
        '''  sets in __objects the obj with key '''
        key = "<{}>.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        ''' save the objects'''
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            dictionay = {key: value.to_dict()
                         for key, value in FileStorage.__objects.items()}
            json.dump(dictionay, f)

    def originalClass(self):
        """
        return the original class specified
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        My_classes = {"BaseModel": BaseModel, "User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review}
        return My_classes

    def reload(self):
        ''' reload from file'''
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                objects = json.load(f)
                objects = {key:
                           self.originalClass()[value["__class__"]](**value)
                           for key, value in objects.items()}
                FileStorage.__objects = objects
