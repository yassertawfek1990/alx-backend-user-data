#!/usr/bin/env python3
"""dsfv dfsvdfvdf dfdfv"""
import os
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """dsfv fdv dfsv dfdf"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """dfvdfsvdf dfvdf df dfsfd"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """dsf dfvfdvdf dfvdsfvdfsv"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """dfsv  fdvdfvdf fd dffsdsdf"""
        return None

    def session_cookie(self, request=None) -> str:
        """dsfvdf dfsv dfv df"""
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
