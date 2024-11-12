from sqlmodel import Session, select
from .model import Industry


# Crear un rubro
def create_industry(industry: Industry, session: Session):
    session.add(industry)
    session.commit()
    session.refresh(industry)
    return industry
    
# Obtener rubro por ID
def get_industry_by_id(industry_id: int, session: Session):
    return session.get(Industry, industry_id)
    
# Obtener rubro por nombre
def get_industry_by_name(name: str, session: Session):
    statement = select(Industry).where(Industry.name == name)
    return session.exec(statement).first()

# Listar todos los rubros
def list_industries(session: Session):
    statement = select(Industry)
    return session.exec(statement).all()

# Actualizar un rubro
def update_industry(industry_id: int, industry_data: dict, session: Session):
    industry = session.get(Industry, industry_id)
    if industry:
        for key, value in industry_data.items():
            setattr(industry, key, value)
        session.add(industry)
        session.commit()
        session.refresh(industry)
        return industry
    return None
    
# Eliminar rubro
def delete_industry(industry_id: int, session: Session):
    industry = session.get(Industry, industry_id)
    if industry:
        session.delete(industry)
        session.commit()
        return True
    return False