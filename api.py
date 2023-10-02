from fastapi import FastAPI
from todo import todo_router

app = FastAPI()


# home route -> hello world message
@app.get('/')
async def hello():
    return {"message" : "Hello, World"}


# including todorouter APIRoute to fast api so that uvicorn can handle that route
app.include_router(todo_router)
