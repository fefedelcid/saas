from sqlmodel import Session, SQLModel, create_engine
from backend import models
from os import getenv

# Configurar la base de datos
DB_URI = getenv("DATABASE_URI")
engine = create_engine(DB_URI, echo=True)

# Crear las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session