from fastapi import Depends, FastAPI
from . import models,schemas
from .database import engine,SessionLocal
from sqlalchemy.orm import Session



models.Base.metadata.create_all(engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app=FastAPI()

@app.post('/blog')
def create_blog(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog  =models.Blog(title = request.title, body = request.body, published = request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
