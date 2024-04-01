from fastapi import Depends, FastAPI, HTTPException,status
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

@app.get('/blog')
def get_all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def get_blog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    return blog

@app.put('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def update_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    blog.update(values={request},synchronize_session=False)
    db.commit()
    return "updated"

@app.delete('blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_blog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    blog.delete(synchronize_session=False)
    
    return "deleted"