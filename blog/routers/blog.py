import re
from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..repository import blog


router = APIRouter(prefix='/blog',tags=['blogs'])



@router.post('/blog',status_code = status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session = Depends(get_db)):
    return blog.create(request,db)

@router.get('')
def get_all_blogs(db:Session = Depends(get_db)):
    return blog.get_all(db)

@router.get('/{id}')
def get_blog(id:int,db:Session = Depends(get_db)):
    return blog.get(id,db)

@router.put('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def update_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db)):
    return blog.update(id,request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session = Depends(get_db)):
    return blog.delete(id,db)