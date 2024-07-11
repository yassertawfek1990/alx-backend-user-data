#!/usr/bin/env python3
"""sdv dfvsf df  dfs"""
import hashlib
from models.base import Base


class User(Base):
    """dfv df df dfgbhkjdv"""

    def __init__(self, *args: list, **kwargs: dict):
        """dfvkl kjlndlfv nkjldf"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """dfv dfvdfv"""
        return self._password

    @password.setter
    def password(self, pwd: str):
        """dfvdf dfvdf fd df"""
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """dfvdf dfvdfvdfv dfdf"""
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """dsvbj kjjkln sdkjlcn kjnjklds"""
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)
