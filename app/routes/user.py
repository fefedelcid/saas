from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.security import create_access_token, verify_password
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


# Ruta para registro de usuario
@user_router.post('/register')
def register(user: User, session: Session = Depends(get_session)):
    existing_user = get_user_by_id(user.id, session)
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya se encuentra registrado.")

    existing_user = get_user_by_username(user.username, session)
    if existing_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya fue tomado.")
    return create_user(user, session)


# Ruta para login
@user_router.post('/login')
def login(username: str, password: str, session: Session = Depends(get_session)):
    user = get_user_by_username(username, session)
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Usuario o contraseña inválidos.")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


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