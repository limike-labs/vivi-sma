"""
Rutas REST de la entidad Categoria.

Responsabilidad: recibir la request, delegar la lógica de negocio en
app.services.categoria_service, y devolver la respuesta validada por los
esquemas de app.schemas.categoria. No contiene lógica de negocio ni de
conexión: eso vive en app/services/categoria_service.py y
app/db/session.py respectivamente.

Flujo: Router (este módulo) → Service → SQLAlchemy → PostgreSQL.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.categoria import CategoriaCreate, CategoriaRead, CategoriaUpdate
from app.services import categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.get("", response_model=list[CategoriaRead])
def listar_categorias(db: Session = Depends(get_db)):
    """Devuelve las categorías principales, ordenadas por id."""
    return categoria_service.listar_categorias(db)


@router.get("/{categoria_id}", response_model=CategoriaRead)
def obtener_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Devuelve una categoría puntual por id."""
    try:
        return categoria_service.obtener_categoria(db, categoria_id)
    except categoria_service.CategoriaNoEncontrada as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        ) from exc


@router.post("", response_model=CategoriaRead, status_code=status.HTTP_201_CREATED)
def crear_categoria(payload: CategoriaCreate, db: Session = Depends(get_db)):
    """Crea una nueva categoría."""
    try:
        return categoria_service.crear_categoria(db, payload)
    except categoria_service.NombreDuplicado as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe una categoría con ese nombre",
        ) from exc


@router.put("/{categoria_id}", response_model=CategoriaRead)
def actualizar_categoria(
    categoria_id: int, payload: CategoriaUpdate, db: Session = Depends(get_db)
):
    """Reemplaza nombre y descripción de una categoría existente."""
    try:
        return categoria_service.actualizar_categoria(db, categoria_id, payload)
    except categoria_service.CategoriaNoEncontrada as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        ) from exc
    except categoria_service.NombreDuplicado as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe una categoría con ese nombre",
        ) from exc


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Elimina una categoría existente."""
    try:
        categoria_service.eliminar_categoria(db, categoria_id)
    except categoria_service.CategoriaNoEncontrada as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada",
        ) from exc
    return None
