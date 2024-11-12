from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.db.session import get_session

from .model import Detail
from .middleware import (
    create_detail,        # POST
    get_detail_by_id,     # GET
    list_details,         # GET
    update_detail,        # PUT
    delete_detail         # DELETE
)

rDetail = APIRouter()

@rDetail.post('/')
def create_new_detail(detail: Detail, session: Session = Depends(get_session)):
    db_detail = get_detail_by_id(detail.id, session)
    if db_detail:
        raise HTTPException(status_code=400, detail="El detalle ya se encuentra registrado.")
    return create_detail(detail, session)


@rDetail.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    detail = get_detail_by_id(id, session)
    if not detail:
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return detail


@rDetail.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_details(session)


@rDetail.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    detail = update_detail(id, data, session)
    if not detail:
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return detail


@rDetail.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_detail(id, session):
        raise HTTPException(status_code=404, detail="Detalle no encontrado.")
    return {"message": "El detalle fue eliminado exitosamente."}