from sqlmodel import SQLModel, Field, Relationship, text
from typing import Optional, List
from datetime import datetime

class Movement(SQLModel, table=True):
    __tablename__ = "movimientos"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"),}) # Fecha de la venta
    total: float # Monto total de la venta
    payment: str # Método de pago

    # Relaciones con User y Details
    user_id: int = Field(foreign_key="usuarios.id")
    user: Optional["User"] = Relationship(back_populates="movements") # type: ignore

    # Relación 1-M movimiento-detalles
    details: Optional[List["Detail"]] = Relationship(back_populates="movement") # type: ignore