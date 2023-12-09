#!/usr/bin/python3
''' define class User '''
from models.base_model import BaseModel


class User(BaseModel):
    ''' Represent the class User '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
