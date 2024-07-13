from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .dependencies import get_db
from .schemas import User, UserCreate, UserUpdate
from .service import create_user, get_user, get_users, update_user, delete_user
from typing import Annotated

router = APIRouter()

@router.post("/user", response_model=User)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db=db, user=user)

@router.get("/user/{user_id}", response_model=User)
def get_user_endpoint(
    user_id: str,
    db: Session = Depends(get_db)
):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users", response_model=list[User])
def get_users_endpoint(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(le=100)] = 10,
    db: Session = Depends(get_db)
):
    return get_users(db=db, skip=skip, limit=limit)

@router.put("/user/{user_id}")
def update_user_endpoint(
    user_id: str,
    user_update: Annotated[UserUpdate, Depends()],
    db: Session = Depends(get_db)
):
    db_user = update_user(db=db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return 

@router.delete("/user/{user_id}")
def delete_user_endpoint(
    user_id: str,
    db: Session = Depends(get_db)
):
    db_user = delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
