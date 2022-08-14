from functools import reduce
from threadsnake.core import *

port = get_port(8089)
siteUrl = f'http://localhost:8089/'
markdownFolder = 'markdown'

app = Application(port)
app.configure(static_files('static'))
app.configure(serve_static_markdown(markdownFolder))

def formatpage(filename:str, params:Dict[str, str]) -> str:
    with open(filename, 'r', encoding='latin1') as f:
        data = f.read()
        for p in params:
            data = data.replace(f"[{p}]", params[p])
        return data
        
    

@app.get('/')
def main(app:Application, req:HttpRequest, res:HttpResponse):
    files = [[j for j in i[2]] for i in os.walk(markdownFolder)]
    files = [re.sub(r'\.[\w\W]+$', '', i) for i in reduce(lambda a,b: a+b, files)]
    files = [(i, i.replace('_', ' ').replace(os.sep, ' >> ')) for i in files]
    links = reduce(lambda a,b: a+b, ['<a href="{0}" target="frame">{1}</a><br/>'.format(i[0], i[1]) for i in files])
    params = {"Title":"Page", "Header":"Threadsnake", "Navs":links}
    res.html(formatpage('index.html', params))

app.wait_exit(f'Navigate to {siteUrl}. Press [Enter] to exit.')