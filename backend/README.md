# VIVÍ SMA — Backend

Backend de VIVÍ SMA construido con **FastAPI**. Estado actual: **Etapa 1** (servidor funcionando, endpoint de verificación, documentación automática) + **Etapa 2** (cimientos de base de datos: PostgreSQL, SQLAlchemy, psycopg y Alembic) + **Etapa 3** (entidad Categoría con endpoints REST). Todavía no incluye autenticación ni otros módulos de negocio (negocios, usuarios, eventos como entidad, etc.) — eso corresponde a etapas posteriores, según el Prompt Master.

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

### 4.1. Aplicar las migraciones (Etapa 2 y 3)

Con `.env` ya configurado y PostgreSQL corriendo:

```bash
alembic upgrade head
```

Esto crea la tabla `categorias` y carga las 8 categorías principales de VIVÍ SMA. Es un paso único (o cada vez que haya migraciones nuevas), no hace falta repetirlo en cada arranque del servidor.

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

### 6.2. Categorías (Etapa 3)

Con la migración aplicada (ver más abajo), el backend ya expone las 8 categorías principales de VIVÍ SMA:

```
GET    /categorias          → lista las 8 categorías
GET    /categorias/{id}     → una categoría puntual
POST   /categorias          → crea una categoría (409 si el nombre ya existe)
PUT    /categorias/{id}     → reemplaza nombre y descripción
DELETE /categorias/{id}     → elimina una categoría
```

Todos aparecen documentados en `/docs`.

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
│   ├── main.py            → Instancia de FastAPI + endpoints propios + registro de routers
│   ├── core/
│   │   └── config.py       → Configuración centralizada (variables de entorno)
│   ├── db/
│   │   └── session.py      → Conexión SQLAlchemy + psycopg, Base declarativa
│   ├── models/
│   │   └── categoria.py    → Modelo SQLAlchemy Categoria (Etapa 3)
│   ├── schemas/
│   │   └── categoria.py    → Esquemas Pydantic de Categoria (Etapa 3)
│   └── routers/
│       └── categorias.py   → Endpoints REST de Categoria (Etapa 3)
├── alembic/                    → Migraciones (incluye la de categorias)
├── alembic.ini
├── .env.example                → Ejemplo de configuración sin credenciales reales
├── requirements.txt
├── .gitignore
└── README.md
```

En etapas posteriores esta estructura crecerá con nuevas entidades (negocios, usuarios, eventos, etc.), cada una siguiendo el mismo patrón: modelo en `app/models/`, esquema en `app/schemas/`, rutas en `app/routers/`.

## Categorías (Etapa 3)

La entidad `Categoria` representa las 8 categorías principales de VIVÍ SMA (Gastronomía, Alojamiento, Turismo, Comercios, Servicios, Salud y bienestar, Transporte, Eventos). Campos: `id`, `nombre` (único), `descripcion`.

- **Modelo** (`app/models/categoria.py`): define la tabla `categorias` en PostgreSQL.
- **Esquemas** (`app/schemas/categoria.py`): `CategoriaCreate`, `CategoriaUpdate`, `CategoriaRead` — separan la validación de la API del modelo de base de datos.
- **Rutas** (`app/routers/categorias.py`): implementan `GET /categorias`, `GET /categorias/{id}`, `POST /categorias`, `PUT /categorias/{id}` y `DELETE /categorias/{id}`, usando `get_db()` de `app/db/session.py` — nunca lógica de conexión propia.
- **Migración** (`alembic/versions/9a974154a336_crear_tabla_categorias.py`): crea la tabla y carga las 8 categorías iniciales como parte del `upgrade()`.

Todavía no existe relación con negocios (eso es de una etapa posterior).

## Conexión a la base de datos (Etapa 2)

La conexión vive exclusivamente en `app/db/session.py`. Ningún endpoint ni `main.py` contiene lógica de conexión directa: todo pasa por:

- `get_db()` — dependencia de FastAPI para obtener una sesión por request (lista para usarse cuando existan endpoints con lógica de negocio).
- `check_database_connection()` — usada por `/health/db` para validar la conexión.

La URL se arma en `app/core/config.py` a partir de las variables `POSTGRES_*` del `.env` (o directamente desde `DATABASE_URL` si se define), siempre con el driver `psycopg` vía el prefijo `postgresql+psycopg://`.

## Uso futuro de Alembic (Etapa 2)

Alembic ya está instalado y configurado (`alembic.ini` + `alembic/env.py`), apuntando a `Base.metadata` de `app/db/session.py` y resolviendo la URL de conexión desde las variables de entorno. La primera migración (Etapa 3) ya crea la tabla `categorias` con sus datos iniciales.

Cuando se agreguen nuevos modelos (etapas posteriores):

```bash
# Importar el nuevo modelo en alembic/env.py, igual que se hizo con Categoria

# Generar una migración a partir de los modelos
alembic revision --autogenerate -m "descripción del cambio"

# Aplicar migraciones pendientes
alembic upgrade head
```

---

## Detener el servidor

`Ctrl + C` en la terminal donde está corriendo.
