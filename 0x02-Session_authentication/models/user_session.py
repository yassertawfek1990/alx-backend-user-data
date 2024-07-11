#!/usr/bin/env python3
"""sdv dfvfv dffdf"""
from models.base import Base


class UserSession(Base):
    """dfv fd v df dfvfdv"""

    def __init__(self, *args: list, **kwargs: dict):
        """df fdfv dfv df dfvf"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
