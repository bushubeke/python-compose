from fastapi import APIRouter,WebSocket,Request,HTTPException

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
ftemps = Jinja2Templates(directory="app/templates")
fileres=APIRouter()



@fileres.get("/addone",response_class=HTMLResponse)
async def add_one(request:Request):
   
    return ftemps.TemplateResponse("addone.html",context={"request": request})
   