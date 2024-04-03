from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas

def create(request:schemas.User,db:Session):
    hashedPassword = request.password
    new_user = models.User(name = request.name , email = request.email, password = hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with {id} not found')
    return user