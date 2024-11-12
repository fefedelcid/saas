from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Product(SQLModel, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)
    unit_price: float
    stock: int
    name: str = Field(index=True, unique=True)
    barcode: Optional[str] = Field(default=None, index=True, unique=True)
    description: Optional[str] = None

    # Relaciones con proveedores y rubros
    supplier_id: Optional[int] = Field(default=None, foreign_key="proveedores.id")
    supplier: Optional["Supplier"] = Relationship(back_populates="products") # type: ignore

    industry_id: Optional[int] = Field(default=None, foreign_key="rubros.id")
    industry: Optional["Industry"] = Relationship(back_populates="products") # type: ignore