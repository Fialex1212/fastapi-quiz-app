from fastapi import HTTPException
from sqlalchemy.orm import Session
from .dependencies import get_db
from .models import User as DBUser
from .schemas import UserCreate, UserUpdate
from sqlalchemy.exc import IntegrityError

def create_user(db: Session, user: UserCreate):
    db_user = DBUser(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: str):
    return db.query(DBUser).filter(DBUser.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(DBUser).offset(skip).limit(limit).all()

# def update_user(db: Session, user_id: str, user_update: UserUpdate):
#     db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
#     if db_user:
#         db_user.username = user_update.username
#         db_user.email = user_update.email
#         db_user.password = user_update.password
#         db.commit()
#         db.refresh(db_user)
#     return db_user

def update_user(db: Session, user_id: str, user_update: UserUpdate):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if db_user:
        if user_update.username is not None:
            db_user.username = user_update.username
        if user_update.email is not None:
            db_user.email = user_update.email
        if user_update.password is not None:
            db_user.password = user_update.password
        
        try:
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Integrity error occurred")
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user