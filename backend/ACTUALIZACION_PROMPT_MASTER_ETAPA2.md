# ACTUALIZACIÓN DEL PROMPT MASTER — ETAPA 2: BASE DE DATOS

## Base de datos

* Se incorpora **PostgreSQL** como base de datos del proyecto.
* La conexión se realiza mediante **SQLAlchemy** (ORM) usando **psycopg**
  (driver psycopg 3) como driver de bajo nivel.
* Arquitectura de datos establecida: `FastAPI → SQLAlchemy → psycopg →
  PostgreSQL`.

## Configuración

* Se crea una configuración centralizada (`app/core/config.py`) basada en
  `pydantic-settings`.
* Las credenciales y parámetros de conexión se leen desde variables de
  entorno, nunca desde código fuente.
* Se agrega `.env.example` como referencia sin credenciales reales; el
  `.env` real ya estaba excluido de Git en el `.gitignore` de la Etapa 1.

## Conexión

* Se crea un módulo independiente y aislado para la conexión a la base de
  datos (`app/db/session.py`), que expone:
  * el `engine` de SQLAlchemy,
  * `SessionLocal` / `get_db()` (dependencia de sesión por request, lista
    para uso futuro en endpoints con lógica de negocio),
  * `Base` (clase declarativa, todavía sin modelos),
  * `check_database_connection()` (verificación técnica de la conexión).
* `main.py` de la Etapa 1 se mantiene intacto en su contenido original
  (título, descripción, versión, endpoint `GET /`) y solo se le agrega el
  nuevo endpoint `GET /health/db`, que delega toda la lógica a
  `app/db/session.py`. Ningún endpoint contiene lógica de conexión
  directa.

## Migraciones

* Se instala y configura **Alembic**, apuntando a `Base.metadata` de
  `app/db/session.py` y resolviendo la URL de conexión dinámicamente
  desde las variables de entorno (no hardcodeada en `alembic.ini`).
* No se generan migraciones de entidades de negocio en esta etapa, ya que
  los modelos definitivos todavía no fueron diseñados.

## Estructura

* Se evoluciona la estructura del backend (que en Etapa 1 era solo
  `app/main.py`) a un esquema modular:

  ```
  backend/
  └── app/
      ├── main.py          (Etapa 1, con el endpoint nuevo agregado)
      ├── core/
      │   └── config.py     (Etapa 2)
      ├── db/
      │   └── session.py    (Etapa 2)
      └── models/             (Etapa 2, preparado, vacío)
  ```

* Se agrega carpeta `alembic/` con su configuración y estructura de
  migraciones (sin migraciones de negocio todavía).

## Dependencias incorporadas

* `sqlalchemy` — ORM y motor de conexión a la base de datos.
* `psycopg[binary]` — driver de PostgreSQL usado por SQLAlchemy.
* `alembic` — sistema de migraciones de esquema.
* `pydantic-settings` — lectura tipada de configuración desde variables
  de entorno.
* `python-dotenv` — soporte para cargar el archivo `.env` en desarrollo.

Se mantuvieron sin cambios las dependencias y versiones ya definidas en
Etapa 1 (`fastapi==0.115.0`, `uvicorn[standard]==0.30.6`).

## Preparación para futuros modelos

* `Base` (SQLAlchemy declarativa) queda definida y lista para que las
  futuras entidades de negocio (usuarios, negocios, categorías,
  eventos, etc.) hereden de ella.
* La carpeta `app/models/` queda creada y documentada, a la espera del
  diseño definitivo de entidades en etapas posteriores.

## Decisiones arquitectónicas relevantes

* Se decidió resolver la URL de conexión de dos formas posibles: variable
  única `DATABASE_URL`, o composición a partir de variables
  `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_HOST` /
  `POSTGRES_PORT` / `POSTGRES_DB`. Esto da flexibilidad para distintos
  entornos (local, staging, producción) sin cambiar código.
* Se decidió NO incluir el `sqlalchemy.url` en `alembic.ini`, resolviendo
  la URL dinámicamente en `alembic/env.py` desde la configuración de la
  app, para evitar cualquier credencial en archivos versionados.
* Se agrega un health check técnico (`GET /health/db`) separado del
  health check general (`GET /`) de la Etapa 1, para no mezclar el
  chequeo de la app con el chequeo de infraestructura de base de datos.
  Esta decisión se señala como potencialmente revisable si en etapas
  posteriores se prefiere consolidar los health checks bajo otro
  criterio.

## Regla permanente

Esta actualización deja registrada conceptualmente la Etapa 2 en el
Prompt Master, sin incluir código completo, conforme a la regla
permanente de documentación establecida.
