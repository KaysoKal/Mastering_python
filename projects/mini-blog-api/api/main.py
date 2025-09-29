from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

def get_connection():
    return psycopg2.connect(
        host="db",
        database="blogdb",
        user="user",
        password="password"
    )

@app.get("/")
def root():
    return {"message": "Mini Blog API"}

@app.get("/posts")
def get_posts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.post("/posts")
def create_post(post: Post):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s) RETURNING id;", (post.title, post.content))
    post_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": post_id, "title": post.title, "content": post.content}
