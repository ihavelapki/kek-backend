import uvicorn

from conf.settings import settings
uvicorn.run('webapp:app', host=settings.server_host, port=settings.server_port)
