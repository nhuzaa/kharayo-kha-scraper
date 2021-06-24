from typing import Optional

import uvicorn
from fastapi import FastAPI
import firebase_admin

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/news/{news_id}")
def get_news(news_id= None):
    return {"news": "abc", "news_id" : news_id}

@app.get("/top-news")
def get_top_news():
    return {"news": "top_abc" }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", debug=True, port=8000)
