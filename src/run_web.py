import asyncio
import uvicorn

from logger import logger
from web.api import app


async def uvicorn_server():
    config = uvicorn.Config(app, port=8080, host="0.0.0.0", reload=True, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    logger.info("Starting uvicorn server")
    asyncio.run(uvicorn_server())
