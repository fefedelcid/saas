

PERMISSIONS = [
    # Usuarios
    {"name": "manage_users", "description": "Gestionar usuarios"},
    {"name": "view_users", "description": "Ver usuarios"},
    # Productos
    {"name": "create_product", "description": "Crear productos"},
    {"name": "edit_product", "description": "Editar productos"},
    {"name": "delete_product", "description": "Eliminar productos"},
    {"name": "view_product", "description": "Ver productos"},
    # Proveedores
    {"name": "create_supplier", "description": "Crear proveedores"},
    {"name": "edit_supplier", "description": "Editar proveedores"},
    {"name": "delete_supplier", "description": "Eliminar proveedores"},
    {"name": "view_supplier", "description": "Ver proveedores"},
    # Rubros
    {"name": "create_industry", "description": "Crear rubros"},
    {"name": "edit_industry", "description": "Editar rubros"},
    {"name": "delete_industry", "description": "Eliminar rubros"},
    {"name": "view_industry", "description": "Ver rubros"},
    # Movimientos
    {"name": "create_movement", "description": "Crear movimientos"},
    {"name": "edit_movement", "description": "Editar movimientos"},
    {"name": "delete_movement", "description": "Eliminar movimientos"},
    {"name": "view_movement", "description": "Ver movimientos"},
    # Detalles
    {"name": "create_detail", "description": "Crear detalles"},
    {"name": "edit_detail", "description": "Editar detalles"},
    {"name": "delete_detail", "description": "Eliminar detalles"},
    {"name": "view_detail", "description": "Ver detalles"},
    # Reportes
    {"name": "view_reports", "description": "Acceder a reportes"},
    {"name": "manage_settings", "description": "Gestionar configuraciones del sistema"}
]


# TODO

# class Permission(SQLModel, table=True):
#     __tablename__ = "permisos"

#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     description: str

#     roles: Optional[List["RolePermission"]] = Relationship(back_populates="permission")


# class Role(SQLModel, table=True):
#     __tablename__ = "roles"

#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str

#     permissions: Optional[List["RolePermission"]] = Relationship(back_populates="role")


# class RolePermission(SQLModel, table=True):
#     __tablename__ = "roles_permisos"

#     role: Role = Relationship(back_populates='permissions')
#     role_id: int = Field(foreign_key="roles.id", primary_key=True)

#     permission: Permission = Relationship(back_populates='roles')
#     permission_id: int = Field(foreign_key="permisos.id", primary_key=True)