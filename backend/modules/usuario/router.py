from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.db.session import get_session
from backend.security import create_access_token, verify_password, get_password_hash

from .model import User
from .middleware import (
    create_user,            # POST
    get_user_by_id,         # GET
    get_user_by_username,   # GET
    list_users,             # GET
    update_user,            # PUT
    delete_user             # DELETE
)

rUser = APIRouter()


# Ruta para registro de usuario
@rUser.post('/register')
def register(user: User, session: Session = Depends(get_session)):
    existing_user = get_user_by_id(user.id, session)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya se encuentra registrado.")

    existing_user = get_user_by_username(user.username, session)
    if existing_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya fue tomado.")
    setattr(user, 'password', get_password_hash(user.password))
    return create_user(user, session)


# Ruta para login
@rUser.post('/login')
def login(username: str, password: str, session: Session = Depends(get_session)):
    user = get_user_by_username(username, session)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Usuario o contraseña inválidos.")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@rUser.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    user = get_user_by_id(id, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@rUser.get('/{username}')
def read_by_name(username: str, session: Session = Depends(get_session)):
    user = get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@rUser.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_users(session)


@rUser.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    user = update_user(id, data, session)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return user


@rUser.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_user(id, session):
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return {"message": "El usuario fue eliminado exitosamente."}