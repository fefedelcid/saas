from sqlmodel import Session, select
from backend.models import Supplier

# Crear un proveedor
def create_supplier(supplier: Supplier, session: Session):
    session.add(supplier)
    session.commit()
    session.refresh(supplier)
    return supplier
    
# Obtener proveedor por ID
def get_supplier_by_id(supplier_id: int, session: Session):
    return session.get(Supplier, supplier_id)
    
# Obtener proveedor por nombre
def get_supplier_by_name(name: str, session: Session):
    statement = select(Supplier).where(Supplier.name == name)
    return session.exec(statement).first()
    
# Obtener proveedor por cuit/cuil
def get_supplier_by_cui(cui: int, session: Session):
    statement = select(Supplier).where(Supplier.cuit_cuil == cui)
    return session.exec(statement).first()
    
# Listar todos los proveedores
def list_suppliers(session: Session):
    statement = select(Supplier)
    return session.exec(statement).all()
    
# Actualizar un proveedor
def update_supplier(supplier_id: int, supplier_data: dict, session: Session):
    supplier = session.get(Supplier, supplier_id)
    if supplier:
        for key, value in supplier_data.items():
            setattr(supplier, key, value)
        session.add(supplier)
        session.commit()
        session.refresh(supplier)
        return supplier
    return None

# Eliminar un proveedor
def delete_supplier(supplier_id: int, session: Session):
    supplier = session.get(Supplier, supplier_id)
    if supplier:
        session.delete(supplier)
        session.commit()
        return True
    return False