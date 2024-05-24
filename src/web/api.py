from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from config import config

app = FastAPI()


@app.get('/')
async def hello():
    return {
        'secret message from .env': config.secret,
        'log file path': config.log_path,
    }


@app.get('/log')
async def log():
    log_path = Path(config.log_path)
    if Path.exists(log_path):
        return FileResponse(log_path)
    return {'error': 'Log file does not exist'}


@app.get('/cron')
async def cron():
    log_path = Path(config.cron_log_path)
    if Path.exists(log_path):
        return FileResponse(log_path)
    return {'error': 'Cron log file does not exist'}
