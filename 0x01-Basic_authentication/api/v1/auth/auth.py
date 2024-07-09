#!/usr/bin/env python3

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    ''' dsc kljnkjsdn ckjnkjnsdkjn ckjnlksdn kljsd'''

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        ''' sdjkcn kjkj sdlkcnj lnlk nsd'''
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # handle * at end of excluded paths
        if path[-1] == '/':
            path = path[:-1]

        ch = False
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '/':
                excluded_path = excluded_path[:-1]
                ch = True

            if excluded_path.endswith('*'):
                ih = excluded_path.rfind('/') + 1
                excluded = excluded_path[ih:-1]

                ih = path.rfind('/') + 1
                th = path[ih:]

                if excluded in th:
                    return False

            if ch:
                ch = False

        path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(
            self,
            request=None
            ) -> str:
        '''Ahjb kdsb jhbkjhbsdcb jhjhbjhb jhjdsc hjsdhk'''
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(
            self,
            request=None
            ) -> TypeVar('User'):
        ''' kjln askjdn kljjnlnk anlksjn lknlkjasc ds'''
        request = Flask(__name__)
        return None
