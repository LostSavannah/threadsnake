from uuid import uuid4
from threadsnake.turbo import Application, HttpResponse, HttpRequest
from threadsnake.http.router import Router

from threadsnake.http.middlewares.requests import accepts, validates_request, \
    requires_parameters, accepts_json

class Resource:
    def __init__(self, name:str) -> None:
        self.name = name
        self.id = str(uuid4())

users = [
    Resource('Erick')
]

router = Router()

@router.get('/')
def get_all(app:Application, req:HttpRequest, res:HttpResponse):
    res.json([i.__dict__ for i in users])

@router.get('/accepts')
@accepts(['text/plain'])
def accepts_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')
    
@router.get('/validates-request')
@validates_request(lambda req:'TestHeader' in req.headers)
def validates_request_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')

@router.get('/requires-parameters')
@requires_parameters(['testParameter'])
def requires_parameters_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')

@router.get('/accepts-json')
@accepts_json
def accepts_json_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')