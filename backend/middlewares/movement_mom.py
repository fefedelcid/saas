from sqlmodel import Session, select
from backend.models import Movement
from datetime import datetime

# Crear un movimiento
def create_movement(movement: Movement, session: Session):
    try:
        setattr(movement, 'created_at', datetime.strptime(movement.created_at, "%Y-%m-%dT%H:%M:%S.%fZ"))
    except TypeError:
        pass
    
    session.add(movement)
    session.commit()
    session.refresh(movement)
    return movement

# Obtener movimiento por ID
def get_movement_by_id(movement_id: int, session: Session):
    return session.get(Movement, movement_id)

# TODO
# Obtener movimiento por fecha
# def get_movement_by_date(name: str, session: Session):
#     statement = select(Movement).where(Movement.name == name)
#     return session.exec(statement).first()

# Listar todos los movimientos
def list_movements(session: Session):
    statement = select(Movement)
    movements = session.exec(statement).all()
    return movements
    
# Actualizar un movimiento
def update_movement(movement_id: int, movement_data: dict, session: Session):
    movement = session.get(Movement, movement_id)
    if movement:
        for key, value in movement_data.items():
            setattr(movement, key, value)
        session.add(movement)
        session.commit()
        session.refresh(movement)
        return movement
    return None

# Eliminar un movimiento
def delete_movement(movement_id: int, session: Session):
    movement = session.get(Movement, movement_id)
    if movement:
        session.delete(movement)
        session.commit()
        return True
    return False