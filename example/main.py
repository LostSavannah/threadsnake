import __main__
from threadsnake.turbo import *
from threadsnake.http.tools.routing import routes_to, routes_to_folder
from threadsnake.http.middlewares.app import *

app:Application = Application(8084)

routes_to_folder(app, "routes")
app.configure(static())

try:
    app.start()
except Exception as e:
    print(e)

