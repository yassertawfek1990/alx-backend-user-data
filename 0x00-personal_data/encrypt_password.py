#!/usr/bin/env python3
"""A module for encrypting passwords.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """nkljnsdvn jnlknsldkvjn lknkljnskldjvn kljn kljnsdlv kj jkj"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """sdvn lkmlksd vkmlm lkm lksdv lkm lklksdkv mmsldk"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
