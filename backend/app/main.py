"""
VIVÍ SMA — API Backend
Etapa 1: Cimientos del backend (servidor + health check).
Etapa 2: Cimientos de base de datos (ver app/core, app/db, app/models).
Etapa 3: Categorías principales (ver app/models/categoria.py,
app/schemas/categoria.py, app/routers/categorias.py).

Este archivo contiene la instancia principal de FastAPI, el endpoint de
verificación general (Etapa 1), el health check técnico de base de datos
(Etapa 2) y el registro del router de categorías (Etapa 3). Todavía no
incluye negocios, usuarios, autenticación ni ningún otro módulo de
dominio — eso corresponde a etapas posteriores, según el Prompt Master
de VIVÍ SMA.
"""

from fastapi import FastAPI

from app.db.session import check_database_connection
from app.routers import categorias

app = FastAPI(
    title="VIVÍ SMA API",
    description="API de VIVÍ SMA — plataforma digital de descubrimiento local de San Martín de los Andes.",
    version="0.1.0",
)

app.include_router(categorias.router)


@app.get("/")
def read_root():
    """
    Endpoint raíz de verificación.
    Permite comprobar que el backend está corriendo y respondiendo.
    """
    return {"message": "VIVÍ SMA API funcionando"}


@app.get("/health/db")
def health_db():
    """
    Health check técnico de la Etapa 2.

    Verifica el camino completo:
    FastAPI -> SQLAlchemy -> psycopg -> PostgreSQL

    No expone lógica de negocio: solo confirma si la conexión a la base
    de datos configurada en las variables de entorno funciona.
    """
    ok, detail = check_database_connection()
    return {
        "database_connected": ok,
        "detail": detail,
    }
