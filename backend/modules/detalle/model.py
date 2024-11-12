from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Detail(SQLModel, table=True):
    __tablename__ = "detalles"

    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="productos.id")
    quantity: int # cantidad vendida
    unit_price: float # precio al que se vendió el producto
    subtotal: float # precio total de esta línea

    # Relación M-1 detalles-movimiento
    movement_id: int = Field(foreign_key="movimientos.id")
    movement: Optional["Movement"] = Relationship(back_populates="details") # type: ignore