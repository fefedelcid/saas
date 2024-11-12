from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Industry(SQLModel, table=True):
    __tablename__ = "rubros"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    details: Optional[str] = None

    # Relación 1-M rubro-productos
    products: List["Product"] = Relationship(back_populates="industry") # type: ignore