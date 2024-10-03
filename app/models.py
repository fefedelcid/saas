from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Supplier(SQLModel, table=True):
    __tablename__ = "proveedores"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    cuit_cuil: str = Field(index=True, unique=True)
    phone_no: Optional[str] = Field(default=None, index=True)

    # Relación 1-M proveedor-productos
    products: List["Product"] = Relationship(back_populates="supplier")


class Industry(SQLModel, table=True):
    __tablename__ = "rubros"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    details: Optional[str] = None

    # Relación 1-M rubro-productos
    products: List["Product"] = Relationship(back_populates="industry")


class Product(SQLModel, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)
    unit_price: float
    stock: int
    name: str = Field(index=True, unique=True)
    barcode: Optional[str] = Field(default=None, index=True, unique=True)
    description: Optional[str] = None

    # Relaciones con proveedores y rubros
    supplier_id: int = Field(foreign_key="proveedores.id")
    industry_id: int = Field(foreign_key="rubros.id")

    supplier: Optional[Supplier] = Relationship(back_populates="products")
    industry: Optional[Industry] = Relationship(back_populates="products")

    # Relación con Detalle
    details: List["Detail"] = Relationship(back_populates="product")


class Detail(SQLModel, table=True):
    __tablename__ = "detalles"

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="productos.id")
    quantity: int # cantidad vendida
    unit_price: float # precio al que se vendió el producto
    subtotal: float # precio total de esta línea

    # Relación con Product
    product: Optional[Product] = Relationship(back_populates="details")

    # Relación M-1 detalles-movimiento
    movement_id: int = Field(foreign_key="movimientos.id")
    movement: Optional["Movement"] = Relationship(back_populates="details")


class Movement(SQLModel, table=True):
    __tablename__ = "movimientos"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now) # Fecha de la venta
    total: float # Monto total de la venta

    # Relaciones con User y Details
    user_id: int = Field(foreign_key="usuarios.id")
    user: Optional["User"] = Relationship(back_populates="movimientos")

    # Relación 1-M movimiento-detalles
    details: List[Detail] = Relationship(back_populates="movement")


class User(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    name: str
    created_at: datetime = Field(default_factory=datetime.now)
    # acc_level: str = Field(default="Vendedor")
    
    # Relación 1-M usuario-movimientos
    movements: List[Movement] = Relationship(back_populates="user")