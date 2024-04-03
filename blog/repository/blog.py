from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas

def create(request:schemas.Blog,db:Session):
    new_blog  =models.Blog(title = request.title, body = request.body, published = request.published,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    return blog

def update(id:int,request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    blog.update(request.dict()) # type: ignore
    db.commit() 
    return "updated"

def delete(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted"