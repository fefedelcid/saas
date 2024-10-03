from fastapi import FastAPI
from app.database import create_db_and_tables

# Rutas
from app.routes.user import user_router
from app.routes.industry import industry_router
from app.routes.movement import movement_router
from app.routes.product import product_router
from app.routes.supplier import supplier_router


app = FastAPI()

# Incluir rutas de usuario
app.include_router(user_router, prefix="/u")
app.include_router(industry_router, prefix="/i")
app.include_router(movement_router, prefix="/m")
app.include_router(product_router, prefix="/p")
app.include_router(supplier_router, prefix="/s")



@app.lifespan("startup")
async def on_startup():
    create_db_and_tables()
    

@app.get("/")
def read_root():
    return {'message':'Hello World!'}