from threadsnake.core import *
app = Application(get_port(80))
@app.get("/main")
def main(app:Application, req:HttpRequest, res:HttpResponse):
	res.end("OK")
