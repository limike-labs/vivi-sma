"""
Configuración centralizada de VIVÍ SMA API.

Todas las credenciales y parámetros sensibles se leen desde variables de
entorno (archivo .env en desarrollo). Este módulo NO contiene credenciales
reales: solo define cómo se leen y valida que existan.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Identidad de la app ---
    APP_NAME: str = "VIVÍ SMA API"
    ENVIRONMENT: str = "development"

    # --- PostgreSQL ---
    # Se puede definir DATABASE_URL directamente, o bien componerla a partir
    # de las variables individuales POSTGRES_*.
    DATABASE_URL: str | None = None

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "vivi_sma"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def sqlalchemy_database_url(self) -> str:
        """
        Devuelve la URL de conexión usada por SQLAlchemy, con el driver
        psycopg (psycopg 3) explícito.

        Si DATABASE_URL fue definida en el .env, se usa tal cual (siempre
        que use el driver psycopg). Caso contrario, se compone a partir de
        las variables POSTGRES_*.
        """
        if self.DATABASE_URL:
            return self.DATABASE_URL

        return (
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Devuelve una instancia cacheada de Settings.
    Usar esta función (no instanciar Settings directamente) para reutilizar
    la misma configuración en toda la app.
    """
    return Settings()
