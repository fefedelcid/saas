from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.database import get_session
from app.models import Product
from app.middlewares.product_mom import (
    create_product,         # POST
    get_product_by_id,      # GET
    get_product_by_name,    # GET
    get_product_by_barcode, # GET
    list_products,          # GET
    update_product,         # PUT
    delete_product         # DELETE
)

product_router = APIRouter()

@product_router.post('/')
def create_new_product(product: Product, session: Session = Depends(get_session)):
    db_product = get_product_by_id(product.id, session)
    if db_product:
        raise HTTPException(status_code=400, detail="El producto ya se encuentra registrado.")
    return create_product(product, session)


@product_router.get('/{id}')
def read_by_id(id: int, session: Session = Depends(get_session)):
    product = get_product_by_id(id, session)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product


@product_router.get('/{name}')
def read_by_name(name: str, session: Session = Depends(get_session)):
    product = get_product_by_name(name, session)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product


@product_router.get('/{barcode}')
def read_by_barcode(barcode: str, session: Session = Depends(get_session)):
    product = get_product_by_barcode(barcode, session)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product


@product_router.get('/')
def read_all(session: Session = Depends(get_session)):
    return list_products(session)


@product_router.put('/{id}')
def update(id: int, data: dict, session: Session = Depends(get_session)):
    product = update_product(id, data, session)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return product


@product_router.delete('/{id}')
def delete(id: int, session: Session = Depends(get_session)):
    if not delete_product(id, session):
        raise HTTPException(status_code=404, detail="Producto no encontrado.")
    return {"message": "El producto fue eliminado exitosamente."}