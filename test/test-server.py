from threadsnake.core import *
from threadsnake.testing import test, run_test
from typing import Callable, Any
import requests
import time
import random
import hashlib

#set_log_config(LogLevel.ALL)
badge_async('threadsnake 0.0.23', title='version')



port:int = get_port(8088)

print(f'listening on port: {port}')

app = Application(port)

#Configuring top level middlewares
app.configure(static_files('static'))
app.configure(session(Session('threadsnake-session-id')))
app.configure(authorization)
app.configure(body_parser)
app.configure(multipart_form_data_parser('temp', 60))
app.configure(json_body_parser)
app.configure(cors)
app.configure(default_headers(build_default_headers({"purpose":"test"})))
#app.configure(identify_client)
app.configure(header_inspector("content-type", lambda a: print(a)))
app.configure(time_measure)
#app.configure(uses_php('php', 'php', 8086))
app.configure(serve_static_markdown('markdown'))

#Configuring routers
app.use_router(routes_to('routers/users'), '/users')

def get_word(length:int = None, vowelChance:float = None):
    length = length or random.randint(2, 10)
    vowelChance = vowelChance or 0.5 + (random.random() / 3)
    vowels = [i for i in 'aeiou']
    consonants = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in vowels]
    res = []
    for i in range(length):
        if random.random() > vowelChance:
            res.append(random.choice(consonants))
        else:
            res.append(random.choice(vowels))
    return ''.join(res)

def get_file():
    return 'this is a file'.encode('latin1')

def get_hash(data):
    return hashlib.md5(data).hexdigest()

@app.get('/test-api/querypath/{param}')
def test_querypath(app:Application, req:HttpRequest, res:HttpResponse):
    res.end(req.params['param'])

@app.get('/test-api/querystring')
@requires_parameters(['param'])
def test_querystring(app:Application, req:HttpRequest, res:HttpResponse):
    res.end(req.params['param'])

@app.get('/test-api/pass')
@requires_parameters(['param'])
def test_querystring(app:Application, req:HttpRequest, res:HttpResponse):
    res.end(req.params['param'])

@app.post('/test-api/multipart-form-data')
@requires_parameters(['param'])
def test_multipart_form_data(app:Application, req:HttpRequest, res:HttpResponse):
    res.end(req.params['param'])

@app.post('/test-api/multipart-form-data/file')
def test_multipart_form_data_file(app:Application, req:HttpRequest, res:HttpResponse):
    if len(req.files) > 0:
        with open([i for i in req.files.values()][0]['tempFilePath'], 'rb') as file:
            res.end(get_hash(file.read()))
    else:
        res.end('')


#TEST
@test({"parameter":get_word}, True)
def when_param_sent_via_querypath_on_get_it_is_returned_as_response(parameter:str = ''):
    url = f'http://localhost:{port}/test-api/querypath/{parameter}'
    return requests.get(url).text == parameter
    
@test({"parameter":get_word}, True)
def when_param_sent_via_querystring_on_get_it_is_returned_as_response(parameter:str = ''):
    url = f'http://localhost:{port}/test-api/querystring?param={parameter}'
    return requests.get(url).text == parameter

@test({"parameter":get_word}, True)
def when_param_sent_via_pass_on_get_it_is_returned_as_response(parameter:str = ''):
    url = f'http://localhost:{port}/test-api/param:{parameter}/pass'
    return requests.get(url).text == parameter

@test({"multipartParameter": get_word}, True)
def when_param_sent_via_multipart_on_post_it_is_ok(multipartParameter:str = ''):
    url = f'http://localhost:{port}/test-api/multipart-form-data'
    return requests.post(url, files={"param": (None, multipartParameter)}).text == multipartParameter

@test({"fileContent": get_file}, True)
def when_file_sent_via_multipart_on_post_it_is_ok(fileContent:str = ''):
    url = f'http://localhost:{port}/test-api/multipart-form-data/file'
    contentHash = get_hash(fileContent)
    return contentHash == requests.post(url, files={"file": ("testfile.txt", fileContent)}).text

try:
    app.start()
    time.sleep(1)
    run_test()
except Exception as e:
    print(e)
finally:
    app.stop()