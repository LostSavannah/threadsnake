import asyncio
from threadsnake.turbo import Application
from threadsnake.http.tools.routing import routes_to_folder

import os

app = Application(9090)
routes_to_folder(app, 'routers')

async def run_test_server_and_test():
    task = asyncio.create_task(app.run())
    os.system('pytest')
    task.cancel()

asyncio.run(run_test_server_and_test())