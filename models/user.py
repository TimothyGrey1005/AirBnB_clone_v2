#!/usr/bin/python3
"""This file defines the User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class represents a user for MySQL database.

    It inherits from the SQLAlchemy Base and the links to the MySQL users table.

    Attributes:
        __tablename__ (str): MySQL table to store users.
        email: (sqlalchemy String): User email address.
        password (sqlalchemy String): User password.
        first_name (sqlalchemy String): User first name.
        last_name (sqlalchemy String): User last name.
        places (sqlalchemy relationship): User-Place relationship.
        reviews (sqlalchemy relationship): User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
