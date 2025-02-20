#!/usr/bin/env python3
"""dcdd sd  m, ,sdm , msd"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None

if getenv('AUTH_TYPE') == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()

elif getenv('AUTH_TYPE') == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def filter_request():
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
    ]
    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None:
        abort(401)

    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ sdc sdkckl k sdck l sdc"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_request(error) -> str:
    '''sdc sd k ksdd sdcsdds'''

    return jsonify({
        "error": "Unauthorized"
    }), 401


@app.errorhandler(403)
def forbidden_request(error) -> str:
    '''sdc m,s d,cm ,m ,m sdcm ,m ,sdcd'''

    return jsonify({
        "error": "Forbidden"
    }), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
