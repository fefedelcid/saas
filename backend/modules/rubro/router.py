from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.db.session import get_session

from .model import Industry
from .middleware import (
    create_industry,            # POST
    get_industry_by_id,         # GET
    get_industry_by_name,       # GET
    list_industries,            # GET
    update_industry,            # PUT
    delete_industry             # DELETE
)

rIndustry = APIRouter()

@rIndustry.post('/')
def create_new_industry(industry: Industry, session: Session = Depends(get_session)):
    db_industry = get_industry_by_id(industry.id, session)
    if db_industry:
        raise HTTPException(status_code=400, detail="El rubro ya se encuentra registrado.")
    return create_industry(industry, session)


@rIndustry.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    industry = get_industry_by_id(id, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@rIndustry.get('/{name}')
def read_by_name(name: str, session: Session = Depends(get_session)):
    industry = get_industry_by_name(name, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@rIndustry.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_industries(session)


@rIndustry.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    industry = update_industry(id, data, session)
    if not industry:
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return industry


@rIndustry.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_industry(id, session):
        raise HTTPException(status_code=404, detail="Rubro no encontrado.")
    return {"message": "El rubro fue eliminado exitosamente."}