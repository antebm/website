from fastapi import FastAPI, Request
from fastapi import responses
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.routing import request_response

from services import blogpost_service

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    recent_posts = blogpost_service.read_recent()
    return templates.TemplateResponse("index.html", {"request": request, "recent_posts": recent_posts})

@app.get("/posts/{post_id}", response_class=HTMLResponse)
async def read_post(request: Request, post_id: str):
    blogpost = blogpost_service.read_blogpost(post_id)
    return templates.TemplateResponse("post.html", {"request": request, "blogpost": blogpost})