#!/usr/bin/python3
"""This file defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """This class represents a review for MySQL database.

    It inherits from the SQLAlchemy Base and then links to MySQL reviews table.

    Attributes:
        __tablename__ (str): MySQL table name to store Reviews.
        text (sqlalchemy String): Review description.
        place_id (sqlalchemy String): Review's place id.
        user_id (sqlalchemy String): Review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
