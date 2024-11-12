from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from backend.db.session import get_session

from .model import Supplier
from .middleware import (
    create_supplier,        # POST
    get_supplier_by_id,     # GET
    get_supplier_by_name,   # GET
    get_supplier_by_cui,    # GET
    list_suppliers,         # GET
    update_supplier,        # PUT
    delete_supplier         # DELETE
)

rSupplier = APIRouter()

@rSupplier.post('/')
def create_new_supplier(supplier: Supplier, session: Session = Depends(get_session)):
    db_supplier = get_supplier_by_id(supplier.id, session)
    if db_supplier:
        raise HTTPException(status_code=400, detail="El proveedor ya se encuentra registrado.")
    return create_supplier(supplier, session)


@rSupplier.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    supplier = get_supplier_by_id(id, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@rSupplier.get('/{name}')
def read_by_name(name: str, session: Session = Depends(get_session)):
    supplier = get_supplier_by_name(name, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@rSupplier.get('/{cui}')
def read_by_cui(cui: str, session: Session = Depends(get_session)):
    supplier = get_supplier_by_cui(cui, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@rSupplier.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_suppliers(session)


@rSupplier.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    supplier = update_supplier(id, data, session)
    if not supplier:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return supplier


@rSupplier.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_supplier(id, session):
        raise HTTPException(status_code=404, detail="Proveedor no encontrado.")
    return {"message": "El proveedor fue eliminado exitosamente."}