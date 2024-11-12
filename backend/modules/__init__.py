# Models
from .detalle.model import Detail
from .inventario.model import Product
from .movimiento.model import Movement
from .proveedor.model import Supplier
from .rubro.model import Industry
from .usuario.model import User

# Routers
from .detalle.router import rDetail
from .inventario.router import rProduct
from .movimiento.router import rMovement
from .proveedor.router import rSupplier
from .rubro.router import rIndustry
from .usuario.router import rUser