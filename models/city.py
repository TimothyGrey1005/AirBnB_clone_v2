#!/usr/bin/python3
"""This file defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This class represents a city for a MySQL database.

    It inherits from the SQLAlchemy Base and then links to the MySQL cities table.

    Attributes:
        __tablename__ (str): MySQL table name to store Cities.
        name (sqlalchemy String): The City name.
        state_id (sqlalchemy String): The City state id.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
