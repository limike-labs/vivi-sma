"""
Service de la entidad Categoria.

Contiene la lógica de las operaciones sobre categorías (listar, obtener,
crear, actualizar, eliminar) y es quien habla directamente con SQLAlchemy.
No conoce a FastAPI ni construye respuestas HTTP: ante un problema,
levanta una excepción propia (CategoriaNoEncontrada / NombreDuplicado)
que el router traduce a la respuesta HTTP correspondiente.

Flujo: Router → Service (este módulo) → SQLAlchemy → PostgreSQL.
"""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate


class CategoriaNoEncontrada(Exception):
    """Se solicitó una categoría que no existe."""


class NombreDuplicado(Exception):
    """Ya existe una categoría con ese nombre."""


def listar_categorias(db: Session) -> list[Categoria]:
    """Devuelve todas las categorías, ordenadas por id."""
    return db.execute(select(Categoria).order_by(Categoria.id)).scalars().all()


def obtener_categoria(db: Session, categoria_id: int) -> Categoria:
    """Devuelve una categoría por id o levanta CategoriaNoEncontrada."""
    categoria = db.get(Categoria, categoria_id)
    if categoria is None:
        raise CategoriaNoEncontrada()
    return categoria


def crear_categoria(db: Session, payload: CategoriaCreate) -> Categoria:
    """Crea una categoría o levanta NombreDuplicado si el nombre ya existe."""
    categoria = Categoria(**payload.model_dump())
    db.add(categoria)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise NombreDuplicado() from exc
    db.refresh(categoria)
    return categoria


def actualizar_categoria(
    db: Session, categoria_id: int, payload: CategoriaUpdate
) -> Categoria:
    """
    Reemplaza nombre y descripción de una categoría existente.

    Levanta CategoriaNoEncontrada si el id no existe, o NombreDuplicado
    si el nuevo nombre choca con el de otra categoría.
    """
    categoria = obtener_categoria(db, categoria_id)
    categoria.nombre = payload.nombre
    categoria.descripcion = payload.descripcion
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise NombreDuplicado() from exc
    db.refresh(categoria)
    return categoria


def eliminar_categoria(db: Session, categoria_id: int) -> None:
    """Elimina una categoría o levanta CategoriaNoEncontrada si no existe."""
    categoria = obtener_categoria(db, categoria_id)
    db.delete(categoria)
    db.commit()
