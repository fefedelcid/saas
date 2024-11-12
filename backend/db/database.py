from sqlmodel import SQLModel
from backend.modules import User, Detail, Industry, Movement, Product, Supplier
from .session import engine

# Crear las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
