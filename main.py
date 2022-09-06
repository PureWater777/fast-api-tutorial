import random
from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = []


@app.get("/")
async def root():
    return {"data": "string"}


@app.get("/posts")
async def get_posts():
    return {"message": my_posts}


@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = random.randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"posts": post_dict}


@app.get("/posts/{id}")
async def get_post(id: int):
    print(id)
    return {"post_detail": f"Post {id}"}




print(my_posts)

