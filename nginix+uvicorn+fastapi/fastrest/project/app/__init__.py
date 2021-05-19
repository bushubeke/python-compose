
import os

from fastapi import FastAPI,WebSocket,Request,HTTPException
from fastapi.staticfiles import StaticFiles


from .controllers.auth import auth
from .fileresponse.fileres import fileres
from .appsocks.sock import socks

def create_dev_app():
    app=FastAPI()
    
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    
    app.include_router(auth)
    app.include_router(fileres)
    app.include_router(socks)
    return app


def create_prod_app():
    app=FastAPI()
    
    app.mount("/static", StaticFiles(directory="/app/static"), name="static")
    
    app.include_router(auth)
    app.include_router(fileres)
    app.include_router(socks)
    return app