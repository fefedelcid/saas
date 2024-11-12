from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from backend.db.database import create_db_and_tables


# Rutas
from backend.modules import rUser
from backend.modules import rIndustry
from backend.modules import rMovement
from backend.modules import rDetail
from backend.modules import rProduct
from backend.modules import rSupplier


# Inicializo FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Cambiar si el frontend está en otro origen
        "http://localhost:3000",
        "http://localhost:5173"
    ], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluyo rutas de usuario
app.include_router(rUser, prefix="/u", tags=["Usuarios"])
app.include_router(rIndustry, prefix="/i", tags=["Rubros"])
app.include_router(rMovement, prefix="/m", tags=["Movimientos"])
app.include_router(rDetail, prefix="/d", tags=["Detalles"])
app.include_router(rProduct, prefix="/p", tags=["Inventario"])
app.include_router(rSupplier, prefix="/s", tags=["Proveedores"])


@app.on_event("startup")
async def on_startup():
    create_db_and_tables()
    

@app.get("/")
def read_root():
    return {'message':'Hello!'}
