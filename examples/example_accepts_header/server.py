from threadsnake.myhttp.http_classes import HttpRequest, HttpResponse
from threadsnake.pypress_classes import Application, BuildApplication
from threadsnake.middlewares import accepts, static_files
from sys import argv

#tries to retrieve port from command line first argument
port = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else 8109

#convenience method for instancing an application setting middlewares and routers
app = BuildApplication(port, [static_files('./static')], {})

@app.get('/test')
@accepts(['text/plain', 'application/json'])
def callback(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('all is well!')


#It will reponse "BadRequest" if you don't specify the allowed content-type in the request
app.wait_exit()