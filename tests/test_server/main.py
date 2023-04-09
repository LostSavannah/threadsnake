import time
import asyncio
import sys
from threadsnake.turbo import Application
from threadsnake.http.tools.routing import routes_to_folder

from threadsnake.http.middlewares.app import authorization, body_parser, \
    build_default_headers, cors, default_headers, json_body_parser, \
    multipart_form_data_parser, session, static, time_measure

app = Application(9090)

app_middlewares = [
    authorization,
    body_parser,
    default_headers(build_default_headers()),
    cors,
    json_body_parser,
    time_measure,
    multipart_form_data_parser('temp'),
    session('threadsnake-session'),
    static('static'),
]

for middleware in app_middlewares:
    app.configure(middleware)

routes_to_folder(app, 'routers')

async def run_server():
    p:asyncio.subprocess.Process = await asyncio.create_subprocess_exec('pytest')
    app_task = asyncio.create_task(app.run())
    await p.wait()
    app_task.cancel()

if 'server' in sys.argv:
    asyncio.run(app.run())
else:
    asyncio.run(run_server())