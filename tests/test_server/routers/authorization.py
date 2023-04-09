from threadsnake.turbo import Application, HttpResponse, HttpRequest
from threadsnake.http.router import Router

router = Router()

@router.get('/')
def eval_authorization(app:Application, req:HttpRequest, res:HttpResponse):
    res.json(req.authorization)