import os
import uvicorn
from fastapi import FastAPI, Request
import api.routes
from db import settings
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from exceptions import AppExceptionCase, AppException, app_exception_handler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = 'OverSee')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(AppExceptionCase)
def custom_app_exception_handler(request: Request, exc: AppException):
    print(exc)
    return app_exception_handler(request, exc)


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