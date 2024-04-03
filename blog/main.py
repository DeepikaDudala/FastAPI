from fastapi import Depends, FastAPI
from .database import models
from .database.database import engine
from .routers import blog,user



models.Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(router= blog.router)
app.include_router(router= user.router)