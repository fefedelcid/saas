from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.database import get_session

from backend.models import Supplier
from backend.middlewares.supplier_mom import (
    create_supplier,        # POST
    get_supplier_by_id,     # GET
    get_supplier_by_name,   # GET
    get_supplier_by_cui,    # GET
    list_suppliers,         # GET
    update_supplier,        # PUT
    delete_supplier         # DELETE
)

supplier_router = APIRouter()

@supplier_router.post('/')
def create_new_supplier(supplier: Supplier, session: Session = Depends(get_session)):
    db_supplier = get_supplier_by_id(supplier.id, session)
    if db_supplier:
        raise HTTPException(status_code=400, detail="El proveedor ya se encuentra registrado.")
    return create_supplier(supplier, session)


@supplier_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    supplier = get_supplier_by_id(id, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@supplier_router.get('/{name}')
def read_by_name(name: str, session: Session = Depends(get_session)):
    supplier = get_supplier_by_name(name, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@supplier_router.get('/{cui}')
def read_by_cui(cui: str, session: Session = Depends(get_session)):
    supplier = get_supplier_by_cui(cui, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@supplier_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_suppliers(session)


@supplier_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    supplier = update_supplier(id, data, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@supplier_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_supplier(id, session):
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return {"message": "El proveedor fue eliminado exitosamente."}