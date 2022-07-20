from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.v1.router.user_router import router as user_router
from app.v1.router.todo_router import router as todo_router

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(todo_router)