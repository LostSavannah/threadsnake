from threadsnake.core import *
from enum import IntEnum
from hashlib import md5
from uuid import uuid4

r:Router = export(__name__)

class UserStatus(IntEnum):
    NORMAL = 0
    UNVERIFIED = 1
    BLOCKED = 2

class Permissions:
    PUBLIC = "public"
    ADMIN = "admin"

availablePermissions = ["admin"]

#password: 12345678
users = [
    {
        "id":1,"userName":"sa","passwordHash":"1de45228676383368292e756d03da931","passwordExtra":"cd016152", "email":"", "status":UserStatus.NORMAL, "permissions":["admin"], "token":""
    }
]

TOKEN_LENGTH = 8
def get_token():
    return str(uuid4()).replace('-', '').lower()[:TOKEN_LENGTH]

def get_hash(data:str):
    return md5(data.encode('latin1')).hexdigest()

def create_user(userName:str, password:str, email:str):
    global users
    id = max([i["id"] for i in users])
    token = get_token()
    confirmationToken = get_token()
    user = {
        "id":id,
        "userName":userName,
        "passwordHash":get_hash(password + token),
        "passwordExtra":token,
        "email":email,
        "status":UserStatus.UNVERIFIED,
        "token": confirmationToken,
        "permissions":[Permissions.PUBLIC]
    }
    users.append(user)
    return user, "OK"
    
def get_user_password_extra(username:str) -> str:
    global users
    extra = [i['passwordExtra'] for i in users if i['userName'] == username]
    return get_hash(username)[:TOKEN_LENGTH] if len(extra) == 0 else extra[0]
    
def get_user_by_id(id:int):
    global users
    return [i['userName'] for i in users if i['id'] == id]
    
@r.post('/')
@requires_parameters(['username', 'password', 'email'])
def create_user_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    p = req.params
    user, result = create_user(p['username'], p['password'], p['email'])
    res.json(user)

@r.get('/')
def get_all_users_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    res.json([i['userName'] for i in users])
    
@r.get('/{id:int}')
@requires_parameters(['id'])
def get_user_by_id_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    users = get_user_by_id(int(req.params['id']))
    if len(users) > 0:
        res.json(users)
    else:
        res.end(responseCodes.get(404, 'Not found'), 404)
    
@r.get('/{username}/passwordExtra')
@requires_parameters(['username'])
def get_user_password_extra_endpoint(app:Application, req:HttpRequest, res:HttpResponse):
    extra = get_user_password_extra(req.params['username'])
    res.end(extra)