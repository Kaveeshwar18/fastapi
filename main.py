from fastapi import FastAPI
from model import Post
import service

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/analyze-post")
def create_post(data: Post):
    return service.analyze_post(data)

@app.get("/posts")
def read_posts():
    return service.get_posts()