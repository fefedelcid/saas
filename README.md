# SaaS Template
### [FastAPI](https://github.com/fastapi/fastapi) + [SQLModel](https://github.com/fastapi/sqlmodel) + [React](https://github.com/facebook/react)
Este proyecto está diseñado para ayudar a las PyMEs a automatizar y optimizar sus procesos de **contabilidad, inventario y recursos humanos**, logrando así una gestión eficiente, rápida y escalable sin depender de métodos tradicionales.

## 🚀 Objetivo del Proyecto
El objetivo principal es simplificar y mejorar la toma de decisiones en negocios pequeños y medianos, brindándoles una solución de software ERP especializado, accesible y fácil de usar. Con este sistema, las PyMEs pueden integrar y gestionar sus operaciones de manera intuitiva y centralizada, reduciendo tiempos y costos.

## ✨ Funcionalidades Clave
*[EN PROGRESO]*
- **Multi-Tenant:** Cada cliente tiene una base de datos aislada, asegurando privacidad y seguridad en la gestión de datos.
- **Gestión de Contabilidad:** Automatización de tareas contables, facilitando el control de ingresos, egresos y balances financieros.
- **Control de Inventario:** Sistema de inventario que permite el seguimiento y la gestión del stock en tiempo real.
- **Recursos Humanos:** Herramientas de gestión para el seguimiento de empleados, horarios, permisos, y más.
- **Interfaz de Usuario Personalizable:** Los usuarios pueden activar o desactivar módulos según sus necesidades específicas.

## 🛠️ Tecnologías
- Backend: FastAPI y SQLModel para una API robusta y escalable.
- Frontend: React para una experiencia de usuario rápida e interactiva.
- Base de Datos: PostgreSQL, se puede utilizar cualquier otra cambiando la URI.
- Distribución en la Nube: Implementación segura en la nube, permitiendo acceso desde cualquier lugar y dispositivo.

## 🚧 Estructura del Proyecto
Este proyecto se enfoca, principalmente, en el backend y la lógica de negocios. Por lo que tomaré la carpeta `backend` como carpeta root del proyecto.
```
./
├── modules/
│   ├── module_name/
│   │   ├── model.py
│   │   ├── router.py
│   │   └── main.py
├── customer/
│   ├── models/
│   ├── views/
│   └── migrations/
```
Cada módulo del sistema (Contabilidad, Inventario, Recursos Humanos) cuenta con su propio espacio en `./modules/module_name/` para mantener una arquitectura ordenada y facilitar futuras expansiones.
<br/>El directorio `./customer/` sirve para precargar el módulo Custormer (encargado de registrar la información de los clientes), mientras que los módulos de `./modules/` sólo se utilizan según la necesidad del cliente.

## 💡 Instalación (Sin Docker)

1. Clonar el repositorio:
```bash
git clone https://github.com/fefedelcid/saas.git
cd saas/backend
```
2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```
3. Instalar las dependencias:
```bash
pip install -r requirements.txt  # <-- uvicorn fastapi sqlmodel
```
4. Ejecutar el servidor
```bash
fastapi run main.py --host 0.0.0.0 --port 8000
```

## 📝 Licencia
Este proyecto está bajo la [Licencia MIT](https://github.com/fefedelcid/saas/blob/main/LICENSE).
