from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from backend.database import create_db_and_tables


# Rutas
from backend.routes.user import user_router
from backend.routes.industry import industry_router
from backend.routes.movement import movement_router
from backend.routes.detail import detail_router
from backend.routes.product import product_router
from backend.routes.supplier import supplier_router


# Inicializo FastAPI
app = FastAPI()


# Incluyo rutas de usuario
app.include_router(user_router, prefix="/u")
app.include_router(industry_router, prefix="/i")
app.include_router(movement_router, prefix="/m")
app.include_router(detail_router, prefix="/d")
app.include_router(product_router, prefix="/p")
app.include_router(supplier_router, prefix="/s")


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    

@app.get("/")
def read_root():
    return {'message':'Hello World!'}
