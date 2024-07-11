#!/usr/bin/env python3
"""gf gf gfd gf fg gfgf"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """dfg fd gf gf gfsdfv gfs"""
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """sf fsg sf gfs fssdv gfs"""
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized/', strict_slashes=False)
def unauthorized() -> None:
    """fs g gf fsgvsv gfssfg"""
    abort(401)


@app_views.route('/forbidden/', strict_slashes=False)
def forbidden() -> None:
    """sf ggf fssg s fg sgsf"""
    abort(403)
