import asyncio
from threadsnake.turbo import Application
from threadsnake.http.middlewares.app import static

app:Application = Application(8089)

app.configure(static('static'))

asyncio.run(app.run())
