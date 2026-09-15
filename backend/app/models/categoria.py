"""
Modelo SQLAlchemy de la entidad Categoria.

Representa las categorías principales de VIVÍ SMA (Etapa 3). Contiene
exclusivamente los campos definidos en el prompt de esta etapa: id,
nombre y descripcion. No se agregan campos adicionales sin autorización.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    descripcion: Mapped[str] = mapped_column(String(500), nullable=False)
