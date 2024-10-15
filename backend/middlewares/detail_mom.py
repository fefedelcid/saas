from sqlmodel import Session, select
from backend.models import Detail

# Crear un detalle
def create_detail(detail: Detail, session: Session):
    session.add(detail)
    session.commit()
    session.refresh(detail)
    return detail

# Obtener detalle por ID
def get_detail_by_id(detail_id: int, session: Session):
    return session.get(Detail, detail_id)


# Listar todos los detalles
def list_details(session: Session):
    statement = select(Detail)
    details = session.exec(statement).all()
    return details
    
# Actualizar un detalle
def update_detail(detail_id: int, detail_data: dict, session: Session):
    detail = session.get(Detail, detail_id)
    if detail:
        for key, value in detail_data.items():
            setattr(detail, key, value)
        session.add(detail)
        session.commit()
        session.refresh(detail)
        return detail
    return None

# Eliminar un detalle
def delete_detail(detail_id: int, session: Session):
    detail = session.get(Detail, detail_id)
    if detail:
        session.delete(detail)
        session.commit()
        return True
    return False