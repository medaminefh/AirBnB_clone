#!/usr/bin/python3
''' define class Amenity '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Repesent class Review '''
    place_id = ""
    user_id = ""
    text = ""