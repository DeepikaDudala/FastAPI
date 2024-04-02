from fastapi import Depends, FastAPI
from . import models,routers
from .database import engine
from .routers import blog



models.Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(router= blog.router)