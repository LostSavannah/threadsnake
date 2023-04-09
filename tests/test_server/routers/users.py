from uuid import uuid4
from threadsnake.turbo import Application, HttpResponse, HttpRequest
from threadsnake.http.router import Router

class User:
    def __init__(self, name:str) -> None:
        self.name = name
        self.id = str(uuid4())

users = [
    User('Erick')
]

router = Router()

@router.get('/')
def get_all(app:Application, req:HttpRequest, res:HttpResponse):
    res.json([i.__dict__ for i in users])