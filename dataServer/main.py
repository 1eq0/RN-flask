import getopt
import web
import sys
#from web.wsgiserver import CherryPyWSGIServer
#from cherrypy import wsgiserver
from cheroot import wsgi # This replaces the 2 above
from flask import Flask, request, request_started
from functools import wraps

import simplejson as json
makejson = json.dumps
app = Flask(__name__)
makejson = json.dumps

DEFAULT_PORT_NO = 8888

def usageguide():
    print("example Backend-Server")

@app.errorhandler(500)
def internal_servererror(error):
    print (" [!]", error)
    return ("Internal Server Error", 500)

@app.route('/',methods=['GET','POST'])
def ex():
    data = {"message" : "hi"}
    print(makejson(data))
    return makejson(data)

if __name__ == '__main__':
    port = DEFAULT_PORT_NO

    urls = ("/.*", "app")
    apps = web.application(urls, globals())
    server = wsgi.Server(("0.0.0.0", port),app,server_name='localhost')
    print (f"The server is hosted on port:{port}")
    
    try:
        server.start()
	#apps.run(port)
    except KeyboardInterrupt:
        server.stop()