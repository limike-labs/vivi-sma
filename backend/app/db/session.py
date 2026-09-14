"""
Módulo independiente de conexión a la base de datos.

Responsabilidad única: crear el engine de SQLAlchemy (driver psycopg) y
exponer la sesión de base de datos al resto de la app.

Esta capa NO conoce a FastAPI ni a los endpoints: main.py y los routers
consumen `get_db` / `check_database_connection`, nunca al revés.
"""

from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

# echo=False por defecto; activar manualmente si se necesita debug de SQL.
engine = create_engine(
    settings.sqlalchemy_database_url,
    pool_pre_ping=True,  # valida la conexión antes de reutilizarla del pool
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True,
)


class Base(DeclarativeBase):
    """
    Base declarativa de SQLAlchemy.

    Todavía sin modelos: queda preparada para que las entidades de negocio
    (Etapa 3 en adelante) hereden de ella.
    """

    pass


def get_db() -> Generator[Session, None, None]:
    """
    Dependencia de FastAPI para obtener una sesión de base de datos por
    request, garantizando su cierre.

    Uso futuro en un endpoint:
        def endpoint(db: Session = Depends(get_db)): ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_database_connection() -> tuple[bool, str]:
    """
    Verifica que la conexión FastAPI -> SQLAlchemy -> psycopg -> PostgreSQL
    funciona, ejecutando un SELECT 1.

    Devuelve (ok, detalle). No lanza excepciones: las captura y las
    describe, para que el endpoint de health check pueda responder con
    claridad en vez de devolver un error 500 genérico.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True, "Conexión a PostgreSQL exitosa"
    except Exception as exc:  # noqa: BLE001 - queremos capturar cualquier error de conexión
        return False, f"No se pudo conectar a PostgreSQL: {exc}"
