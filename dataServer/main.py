import getopt
import web
import sys
#from web.wsgiserver import CherryPyWSGIServer
#from cherrypy import wsgiserver
from cheroot import wsgi # This replaces the 2 above
from flask import Flask, request, request_started, Response
from functools import wraps

import execute
import simplejson as json

from test import VideoCamera

makejson = json.dumps
app = Flask(__name__)

DEFAULT_PORT_NO = 8888

def usageguide():
    print("example Backend-Server")

@app.errorhandler(500)
def internal_servererror(error):
    print (" [!]", error)
    return ("Internal Server Error", 500)

def gen(camera):
    reps = 0
    status = 'Start'
    while True:
        frame, reps, status = camera.get_frame(reps, status)
        # print(str(reps) + status)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed',methods=['GET','POST'])
def video_feed():
    print("connected")
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/myData',methods=['GET', 'POST'])
def ex():
    data = {
        "message":"hi",
    }
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