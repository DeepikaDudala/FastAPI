from fastapi import APIRouter,status,HTTPException,Depends
from sqlalchemy.orm import Session
from .. import schemas,models
from ..database import get_db

router = APIRouter()



@router.post('/blog',status_code = status.HTTP_201_CREATED,tags=['blogs'])
def create_blog(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog  =models.Blog(title = request.title, body = request.body, published = request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog',tags=['blogs'])
def get_all_blogs(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get('/blog/{id}',tags=['blogs'])
def get_blog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    return blog

@router.put('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def update_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    blog.update(request.dict()) # type: ignore
    db.commit()
    return "updated"

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def delete_blog(id:int,db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with {id} is not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return "deleted"