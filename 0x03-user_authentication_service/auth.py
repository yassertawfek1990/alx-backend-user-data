#!/usr/bin/env python3
"""fgbkjkn nkjdsv jklnlkdsfb"""
import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """kjksdnv kjlnlsdkfv kljdsf"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """jhbkj dfkhhvb jhb dkjfv kdfs"""
    return str(uuid4())


class Auth:
    """nkjl dnfnkljndflkjvn dfsbgf"""

    def __init__(self):
        """jhj kjd sjkjnnfkljvnl kjdfnlv"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """jhkdf kkjfgn kndfkjgn fgb"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        """dfbkjljn lkdfjnvl klksdvn lkdsfjlk"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                return bcrypt.checkpw(
                    password.encode("utf-8"),
                    user.hashed_password,
                )
        except NoResultFound:
            return False
        return False

    def create_session(self, email: str) -> str:
        """kjknlsdkfjnv kljnlkfdjvn klsdfnvlks"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        if user is None:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """sdfjn lkdfsv lknlkdfjb kljdsfv"""
        user = None
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """kj dslfkvj ldfkj nkjdanavvljdfjx"""
        if user_id is None:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """jhdfb kjndfs nlkjndklf vndf"""
        user = None
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        if user is None:
            raise ValueError()
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """dfjvklj nlkdfn vlkjndlkfvn lkjsdf"""
        user = None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            user = None
        if user is None:
            raise ValueError()
        new_password_hash = _hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=new_password_hash,
            reset_token=None,
        )
