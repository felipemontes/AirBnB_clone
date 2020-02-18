#!/usr/bin/python3
''' Review Modules'''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' Class to save review information '''
    place_id = ''
    user_id = ''
    text = ''
