from sqlmodel import Session, select
from .model import Product

# Crear un producto
def create_product(product: Product, session: Session):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

# Obtener producto por ID
def get_product_by_id(product_id: int, session: Session):
    return session.get(Product, product_id)

# Obtener producto por nombre
def get_product_by_name(name: str, session: Session):
    statement = select(Product).where(Product.name == name)
    return session.exec(statement).first()

# Obtener producto por barcode
def get_product_by_barcode(barcode: str, session: Session):
    statement = select(Product).where(Product.barcode == barcode)
    return session.exec(statement).first()

# Listar todos los productos
def list_products(session: Session):
    statement = select(Product)
    products = session.exec(statement).all()
    return products
    
# Actualizar un producto
def update_product(product_id: int, product_data: dict, session: Session):
    product = session.get(Product, product_id)
    if product:
        for key, value in product_data.items():
            setattr(product, key, value)
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
    return None

# Eliminar un producto
def delete_product(product_id: int, session: Session):
    product = session.get(Product, product_id)
    if product:
        session.delete(product)
        session.commit()
        return True
    return False