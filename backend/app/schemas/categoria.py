"""
Esquemas Pydantic de la entidad Categoria.

Separados del modelo SQLAlchemy: estos esquemas validan lo que entra y
sale por la API, sin acoplar la API directamente a la tabla de la base
de datos.
"""

from pydantic import BaseModel, ConfigDict, Field


class CategoriaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: str = Field(..., min_length=1, max_length=500)


class CategoriaCreate(CategoriaBase):
    """Datos requeridos para crear una categoría (POST)."""

    pass


class CategoriaUpdate(CategoriaBase):
    """Datos requeridos para reemplazar una categoría (PUT)."""

    pass


class CategoriaRead(CategoriaBase):
    """Representación de una categoría devuelta por la API."""

    id: int

    model_config = ConfigDict(from_attributes=True)
