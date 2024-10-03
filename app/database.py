from sqlmodel import Session, SQLModel, create_engine

# Configurar la base de datos
DATABASE_URL = "sqlite:///./database/database.db"
engine = create_engine(DATABASE_URL, echo=True)

# Crear las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session