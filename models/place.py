#!/usr/bin/python3
"""Place Module for HBNB project."""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """The class "Place" inherits from "BaseModel" and "Base"."""

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        """Return a list of amenities related to the place."""
        from models import storage
        amenities_list = []
        for item in storage.all(Amenity).values():
            if item.id == self.amenity_ids:
                amenities_list.append(item)
        return amenities_list

    @amenities.setter
    def amenities(self, object):
        """Add an amenity to the amenities list."""
        if type(object) == Amenity:
            self.amenity_ids.append(object.id)
