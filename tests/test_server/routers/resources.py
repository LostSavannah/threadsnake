from uuid import uuid4
from threadsnake.turbo import Application, HttpResponse, HttpRequest
from threadsnake.http.router import Router

from threadsnake.http.middlewares.requests import accepts, validates_request, \
    requires_parameters, accepts_json

from threadsnake.http.middlewares.app import authorization, body_parser, \
    build_default_headers, cors, default_headers, json_body_parser, \
    multipart_form_data_parser, session, static, time_measure


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

accepts(['text/plain'])
@router.get('/accepts')
def accepts_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.end('Ready')
    