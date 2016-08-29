from functools import wraps
from flask import request,jsonify

def login_required(func):

    @wraps(func)
    def decorator_func(*args,**kwargs):
        user        = request.headers.get('user')
        api_key     = request.headers.get('api_key')
        api_secret  = request.headers.get('api_secret')
        hash        = request.headers.get('hash')
        timestamp   = request.headers.get('timestamp')

        if not user or not api_key or not api_secret :
            return jsonify("Error: Invalid Request"),412

        if not hash or not timestamp :
            return jsonify("Error: Invalid Request"), 412




