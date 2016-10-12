from functools import wraps
from flask import request,jsonify
from nishu import get_application_model
import  hmac, hashlib

def auth_required(func):

    @wraps(func)
    def decorator_func(*args,**kwargs):
        user        = request.headers.get('user')
        api_key     = request.headers.get('api_key')
        api_secret  = request.headers.get('api_secret')
        user_hash   = request.headers.get('hash')
        user_timestamp   = request.headers.get('timestamp')

        if not user or not api_key or not api_secret :
            return jsonify("Error: Invalid Request"),412

        if not hash or not user_timestamp or not user_hash:
            return jsonify("Error: Invalid Request"), 412

        server_key = get_key(api_key,user)

        if not server_key:
            return jsonify("key not found"),412

        timestamp_hash = generate_hmac(str(server_key), str(user_timestamp))
        #for get request

        if request.method == 'GET':
            url = request.path + '?' + request.query_string if request.query_string else request.path
            server_hash = generate_hmac(str(timestamp_hash), str(url))
            if hmac.compare_digest(server_hash, user_hash):
                return func(*args, **kwargs)
            else:
                return jsonify("Error : HMAC is not matched"), 412
            #change with the hmac
            # server_hash = base64.base64encode(str(server_key),str(url))
            # if user_hash == server_hash:
            #     return func(*args,**kwargs)

            # else :
                # return jsonify("Error: HMAC is not matched"),412


        if request.method == 'POST':
            #check for file upload
            data = request.data.decode('utf-8')
            server_hash = generate_hmac(str(timestamp_hash),data)
            if hmac.compare_digest(server_hash,user_hash):
                return func(*args, **kwargs)
            else:
                return jsonify("Error : HMAC is not matched"), 412
    return decorator_func



def get_key(api_key,username):
    app_model= get_application_model(api_key)
    #need validation
    server_key = app_model.api_key if username == app_model.username else None
    return server_key


def generate_hmac(key,message):
    hash = hmac.new(key,message.encode('utf-8'),hashlib.sha256).hexdigest()
    return hash
