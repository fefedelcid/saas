from sqlmodel import Session, select
from .model import User
from datetime import datetime

# Crear un usuario
def create_user(user: User, session: Session):
    try:
        setattr(user, 'created_at', datetime.strptime(user.created_at, "%Y-%m-%dT%H:%M:%S.%fZ"))
    except TypeError:
        pass
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Obtener usuario por ID
def get_user_by_id(user_id: int, session: Session):
    return session.get(User, user_id)

# Obtener usuario por nickname
def get_user_by_username(username: str, session: Session):
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()

# Listar todos los usuarios
def list_users(session: Session):
    statement = select(User)
    users = session.exec(statement).all()
    return users
    
# Actualizar un usuario
def update_user(user_id: int, user_data: dict, session: Session):
    user = session.get(User, user_id)
    if user:
        for key, value in user_data.items():
            setattr(user, key, value)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    return None

# Eliminar un usuario
def delete_user(user_id: int, session: Session):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False