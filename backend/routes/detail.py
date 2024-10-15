from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.database import get_session

from backend.models import Detail
from backend.middlewares.detail_mom import (
    create_detail,        # POST
    get_detail_by_id,     # GET
    list_details,         # GET
    update_detail,        # PUT
    delete_detail         # DELETE
)

detail_router = APIRouter()

@detail_router.post('/')
def create_new_detail(detail: Detail, session: Session = Depends(get_session)):
    db_detail = get_detail_by_id(detail.id, session)
    if db_detail:
        raise HTTPException(status_code=400, detail="El detalle ya se encuentra registrado.")
    return create_detail(detail, session)


@detail_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    detail = get_detail_by_id(id, session)
    if not detail:
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return detail


@detail_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_details(session)


@detail_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    detail = update_detail(id, data, session)
    if not detail:
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return detail


@detail_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_detail(id, session):
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return {"message": "El detalle fue eliminado exitosamente."}