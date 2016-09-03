from functools import wraps
from flask import request,jsonify
from nishu import get_application_model
import  hmac, hashlib
def login_required(func):

    @wraps(func)
    def decorator_func(*args,**kwargs):
        user        = request.headers.get('user')
        api_key     = request.headers.get('api_key')
        api_secret  = request.headers.get('api_secret')
        user_hash   = request.headers.get('hash')
        timestamp   = request.headers.get('timestamp')

        if not user or not api_key or not api_secret :
            return jsonify("Error: Invalid Request"),412

        if not hash or not timestamp or not user_hash:
            return jsonify("Error: Invalid Request"), 412

        server_key = get_key(api_key)

        if not server_key:
            return jsonify("key not found"),412


        #for get request

        if request.method == 'GET':
            url = str(request.path)
            #create hash here to compare with user hash
            #api_key and url





def get_key(api_key):
    app_model= get_application_model(api_key)
    #need validation
    server_key = app_model.api_key
    return server_key


def generate_hmac(key,message):

    hash = hmac.new(key,message.encode('utf-8'),hashlib.sha256).digest()

    return hash
