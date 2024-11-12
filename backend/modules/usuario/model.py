from sqlmodel import SQLModel, Field, Relationship, text
from typing import Optional, List
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    name: str
    created_at: datetime = Field(sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"),})
    # acc_level: str = Field(default="Vendedor")
    
    # Relación 1-M usuario-movimientos
    movements: Optional[List["Movement"]] = Relationship(back_populates="user") # type: ignore