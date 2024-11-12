from sqlmodel import Session, create_engine
from os import getenv


# Configurar la base de datos
DB_URI = getenv("DATABASE_URI")
engine = create_engine(DB_URI, echo=True)


def get_session():
    with Session(engine) as session:
        yield session