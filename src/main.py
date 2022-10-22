import os
import uvicorn
from fastapi import FastAPI, Request
import api.routes
from db import settings
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title = 'OverSee')


parent_path = os.path.dirname(os.path.realpath(__file__))

app.mount('/static/', StaticFiles(directory=f'{parent_path}/static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


app.include_router(api.routes.api_router, prefix=settings.API_V_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True, log_level="info")