#!/usr/bin/env python3
""" Msdc lknskdn ckjn kjlnlksd lkj"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GETkjjl sdk nkjn klkj knkjsdckl nknlknsdnlk scd"""
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ Gds cjhbkjbkjsdhc jhbh hjbhjbhjb jhb jhj bhj bkjbhk jh"""
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route("/unauthorized/",
                 strict_slashes=False)
def unauthorized() -> str:
    '''Rjkn lksdcklk knjklnjkl sdn kjjkjnkjsd kjnkjnlk sds'''
    abort(401)


@app_views.route("/forbidden/",
                 strict_slashes=False)
def forbidden() -> str:
    '''jhbkh svd b blkkjnskjd vj jnnknsdjn sdjnl kjnkjljsdvcnln lksd'''
    abort(403)
