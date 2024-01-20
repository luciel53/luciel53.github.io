#!/usr/bin/python3
"""
importing classes and modules
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    module the classes that contains the base
    class for the Airbnb console
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of attributes for public instances
        """
        if len(kwargs) != 0:
            del kwargs["__class__"]

            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")

                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")

                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Method Prints information of an object
        """
        prtn = "[{}] ({}) {}"
        return prtn.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method updates the public instance attribute with date and time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values _dict_ of the instance
        """
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = type(self).__name__
        n_dict["created_at"] = self.created_at.isoformat()
        n_dict["updated_at"] = self.updated_at.isoformat()
        return n_dict
