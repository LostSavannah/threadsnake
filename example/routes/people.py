from typing import Any, Dict, List
from threadsnake.http.router import Router
from threadsnake.turbo import *

people:List[Dict[str, Any]] = [{
    "id":4,
    "name": "papolo"
}]

router:Router = Router()

@router.get('/{id:int}')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    candidates = [i for i in people if i['id'] == int(req.params['id'])]
    if len(candidates) > 0:
        res.json(candidates)
    else:
        res.status(404, 'NotFound')

@router.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    res.json(people)

@router.post('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    id:int = max([int(i['id']) for i in people]) + 1
    data = req.json()
    if data is not None:
        data['id'] = id
        people.append(data)
        res.json(data)
    else:
        bad_request(res)

@router.put('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    new = req.json()
    id:int = int(new['id'])
    data = [person for person in people if person["id"] == id]
    if len(data) > 0:
        data[0].update(new)
        res.json(data[0])
    else:
        not_found(res)
    
@router.delete('/{id:int}')
def dele(app:Application, req:HttpRequest, res:HttpResponse):
    id:int = int(req.params['id'])
    data = [i for i in people if i['id'] == id]
    if len(data) > 0:
        people.remove(data[0])
        res.json(data[0])
    else:
        not_found(res)