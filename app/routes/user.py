from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import User
from app.middlewares.user_mom import (
    create_user,            # POST
    get_user_by_id,         # GET
    get_user_by_username,   # GET
    list_users,             # GET
    update_user,            # PUT
    delete_user             # DELETE
)

user_router = APIRouter()

@user_router.post('/')
def create_new_user(user: User, session: Session = Depends(get_session)):
    db_user = get_user_by_id(user.id, session)
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya se encuentra registrado.")

    db_user = get_user_by_username(user.username, session)
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya fue tomado.")
    return create_user(user, session)


@user_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(id, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@user_router.get('/{username}')
def read_by_name(username: str, session: Session = Depends(get_session)):
    user = get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@user_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_users(session)


@user_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    user = update_user(id, data, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@user_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_user(id, session):
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return {"message": "El usuario fue eliminado exitosamente."}