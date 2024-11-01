from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.auth import auth_router
from config.database import engine, Base

app = FastAPI()
app.title = "My app with FastAPI"
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(auth_router)
app.include_router(movie_router)
Base.metadata.create_all(bind=engine)

