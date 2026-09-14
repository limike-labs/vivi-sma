# VIVÍ SMA — Backend

Backend de VIVÍ SMA construido con **FastAPI**. Estado actual: **Etapa 1** (servidor funcionando, endpoint de verificación, documentación automática) + **Etapa 2** (cimientos de base de datos: PostgreSQL, SQLAlchemy, psycopg y Alembic). Todavía no incluye autenticación ni ningún módulo de negocio (usuarios, negocios, categorías, eventos, etc.) — eso corresponde a etapas posteriores, según el Prompt Master.

Arquitectura actual:

```
Frontend → API → FastAPI → SQLAlchemy → psycopg → PostgreSQL
```

---

## Requisitos

- Python 3.9 o superior instalado en tu sistema.
- Una instancia de **PostgreSQL** corriendo (local o remota), con una base de datos creada (ver "Preparar PostgreSQL" más abajo). Necesaria para `/health/db`; el resto del servidor funciona igual sin ella.

---

## Preparar PostgreSQL (Etapa 2)

Crear la base de datos que va a usar el backend, por ejemplo:

```sql
CREATE DATABASE vivi_sma;
```

## Variables de entorno (Etapa 2)

Copiar el ejemplo y completar con las credenciales reales:

```bash
cp .env.example .env
```

Editar `.env` con los datos de conexión (usuario, contraseña, host, puerto, nombre de la base). El archivo `.env` está excluido de Git (ver `.gitignore`) y **nunca** debe subirse al repositorio.

---

## Cómo ejecutar el backend localmente

### 1. Entrar en la carpeta `backend`

```bash
cd backend
```

### 2. Crear un entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

Vas a ver `(venv)` al principio de la línea de tu terminal cuando esté activado correctamente.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

`--reload` hace que el servidor se reinicie automáticamente cada vez que guardás un cambio en el código — útil solo para desarrollo local, no se usa en producción.

### 6. Acceder al endpoint

Con el servidor corriendo, abrí en el navegador:

```
http://127.0.0.1:8000/
```

Deberías ver:

```json
{"message": "VIVÍ SMA API funcionando"}
```

### 6.1. Verificar la conexión a PostgreSQL (Etapa 2)

```
http://127.0.0.1:8000/health/db
```

Si `.env` está bien configurado y PostgreSQL está corriendo, deberías ver:

```json
{"database_connected": true, "detail": "Conexión a PostgreSQL exitosa"}
```

Si no, el mismo endpoint devuelve `database_connected: false` con el detalle del error, sin romper el resto del servidor.

### 7. Acceder a la documentación automática

FastAPI genera automáticamente dos interfaces de documentación interactiva, sin que tengamos que escribir nada extra:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Desde `/docs` podés probar el endpoint directamente desde el navegador, sin necesidad de Postman ni curl.

---

## Estructura actual

```
backend/
├── app/
│   ├── main.py            → Instancia de FastAPI + endpoints GET / y GET /health/db
│   ├── core/
│   │   └── config.py       → Configuración centralizada (variables de entorno)
│   ├── db/
│   │   └── session.py      → Conexión SQLAlchemy + psycopg, Base declarativa
│   └── models/               → Preparado para futuros modelos (vacío por ahora)
├── alembic/                    → Migraciones (sin migraciones de negocio todavía)
├── alembic.ini
├── .env.example                → Ejemplo de configuración sin credenciales reales
├── requirements.txt
├── .gitignore
└── README.md
```

En etapas posteriores esta estructura crecerá con carpetas como `api/`, `schemas/`, `services/` y `tests/`, y `app/models/` empezará a llenarse con las entidades de negocio reales.

## Conexión a la base de datos (Etapa 2)

La conexión vive exclusivamente en `app/db/session.py`. Ningún endpoint ni `main.py` contiene lógica de conexión directa: todo pasa por:

- `get_db()` — dependencia de FastAPI para obtener una sesión por request (lista para usarse cuando existan endpoints con lógica de negocio).
- `check_database_connection()` — usada por `/health/db` para validar la conexión.

La URL se arma en `app/core/config.py` a partir de las variables `POSTGRES_*` del `.env` (o directamente desde `DATABASE_URL` si se define), siempre con el driver `psycopg` vía el prefijo `postgresql+psycopg://`.

## Uso futuro de Alembic (Etapa 2)

Alembic ya está instalado y configurado (`alembic.ini` + `alembic/env.py`), apuntando a `Base.metadata` de `app/db/session.py` y resolviendo la URL de conexión desde las variables de entorno. **Todavía no hay migraciones**, porque no se diseñaron los modelos de negocio.

Cuando existan modelos (etapas posteriores):

```bash
# Generar una migración a partir de los modelos
alembic revision --autogenerate -m "descripción del cambio"

# Aplicar migraciones pendientes
alembic upgrade head
```

---

## Detener el servidor

`Ctrl + C` en la terminal donde está corriendo.
