import asyncio
from threadsnake.turbo import Application
from threadsnake.http.tools.routing import routes_to_folder

app = Application(9090)
routes_to_folder(app, 'routers')

async def run_server():
    p:asyncio.subprocess.Process = await asyncio.create_subprocess_exec('pytest')
    app_task = asyncio.create_task(app.run())
    await p.wait()
    app_task.cancel()

asyncio.run(run_server())