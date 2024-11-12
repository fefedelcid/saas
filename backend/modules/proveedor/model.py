from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Supplier(SQLModel, table=True):
    __tablename__ = "proveedores"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    cuit_cuil: str = Field(index=True, unique=True)
    phone_no: Optional[str] = Field(default=None, index=True)

    # Relación 1-M proveedor-productos
    products: List["Product"] = Relationship(back_populates="supplier") # type: ignore