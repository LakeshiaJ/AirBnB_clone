#!/usr/bin/python3
"""This module creates a place class"""

from model.base_model import Basemodel

classplace(Basemodel):
    """class for managing place objects"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = o.o
    amenity_ids = []
