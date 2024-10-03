from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import Movement
from app.middlewares.movement_mom import (
    create_movement,        # POST
    get_movement_by_id,     # GET
    list_movements,         # GET
    update_movement,        # PUT
    delete_movement         # DELETE
)

movement_router = APIRouter()

@movement_router.post('/')
def create_new_movement(movement: Movement, session: Session = Depends(get_session)):
    db_movement = get_movement_by_id(movement.id, session)
    if db_movement:
        raise HTTPException(status_code=400, detail="El movimiento ya se encuentra registrado.")
    return create_movement(movement, session)


@movement_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    movement = get_movement_by_id(id, session)
    if not movement:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado.")
    return movement


@movement_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_movements(session)


@movement_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    movement = update_movement(id, data, session)
    if not movement:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado.")
    return movement


@movement_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_movement(id, session):
        raise HTTPException(status_code=404, detail="Movimiento no encontrado.")
    return {"message": "El movimiento fue eliminado exitosamente."}