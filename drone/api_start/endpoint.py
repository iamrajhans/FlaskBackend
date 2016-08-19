from drone.api_start import api

@api.route('/',methods=['GET'])
def start():
    return "Hello World"