from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.database import get_session

from backend.models import Industry
from backend.middlewares.industry_mom import (
    create_industry,            # POST
    get_industry_by_id,         # GET
    get_industry_by_name,       # GET
    list_industries,            # GET
    update_industry,            # PUT
    delete_industry             # DELETE
)

industry_router = APIRouter()

@industry_router.post('/')
def create_new_industry(industry: Industry, session: Session = Depends(get_session)):
    db_industry = get_industry_by_id(industry.id, session)
    if db_industry:
        raise HTTPException(status_code=400, detail="El rubro ya se encuentra registrado.")
    return create_industry(industry, session)


@industry_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    industry = get_industry_by_id(id, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@industry_router.get('/{name}')
def read_by_name(name: str, session: Session = Depends(get_session)):
    industry = get_industry_by_name(name, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@industry_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_industries(session)


@industry_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    industry = update_industry(id, data, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@industry_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_industry(id, session):
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return {"message": "El rubro fue eliminado exitosamente."}