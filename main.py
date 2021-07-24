import os
from fastapi import FastAPI, Request
from fastapi import responses
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.routing import request_response

from data import db_session
from services import blogpost_service


def setup_db():
    db_file = os.path.join(os.path.dirname(__file__),
                'db',
                'website.sqlite')

    db_session.global_init(db_file)

app = FastAPI()

setup_db()

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

@app.get("{full_path:path}", response_class=HTMLResponse)
async def no_content(request: Request, full_path: str):
    return templates.TemplateResponse("404.html", {"request": request })