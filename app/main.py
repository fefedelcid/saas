from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import create_db_and_tables
from app.models import User
from app.security import SECRET_KEY, ALGORITHM
from jwt.exceptions import PyJWTError
import jwt

# Rutas
from app.routes.user import user_router
from app.routes.industry import industry_router
from app.routes.movement import movement_router
from app.routes.product import product_router
from app.routes.supplier import supplier_router


# Inicializo FastAPI
app = FastAPI()


# Configuro JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token.")
        return username
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token.")


# Incluyo rutas de usuario
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


@app.get("/me")
def read_user(user: User = Depends(get_current_user)):
    return user