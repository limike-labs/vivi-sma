# ACTUALIZACIÓN DEL PROMPT MASTER — ETAPA 3: CATEGORÍAS PRINCIPALES

## Nueva entidad: Categoria

* Se incorpora la primera entidad de negocio real del backend: `Categoria`.
* Campos exclusivos, tal como fue definido: `id`, `nombre`, `descripcion`.
  No se agregaron campos adicionales.
* `nombre` se definió como único a nivel de base de datos (constraint
  `UNIQUE`), para evitar categorías duplicadas. Es una decisión de
  integridad de datos, no un campo nuevo — se señala igual porque no
  estaba explícitamente pedida en el prompt de la etapa.

## Estructura de datos

* Tabla PostgreSQL: `categorias` (`id` serial/PK, `nombre` varchar(100)
  único, `descripcion` varchar(500)).
* Modelo SQLAlchemy en `app/models/categoria.py`, heredando de `Base`
  (definida en la Etapa 2).

## Esquemas (Pydantic)

* `app/schemas/categoria.py`:
  * `CategoriaBase` — campos comunes con validación de longitud.
  * `CategoriaCreate` — entrada para `POST`.
  * `CategoriaUpdate` — entrada para `PUT` (reemplazo completo).
  * `CategoriaRead` — salida de la API, incluye `id`.
* Los esquemas están desacoplados del modelo de base de datos: la API
  nunca expone ni recibe el modelo SQLAlchemy directamente.

## Endpoints

Implementados en `app/routers/categorias.py`, registrados en `main.py`
vía `app.include_router(categorias.router)`:

* `GET /categorias` — lista todas las categorías, ordenadas por id.
* `GET /categorias/{id}` — devuelve una categoría o 404 si no existe.
* `POST /categorias` — crea una categoría; devuelve 201, o 409 si el
  nombre ya existe.
* `PUT /categorias/{id}` — reemplaza nombre y descripción; 404 si no
  existe, 409 si el nuevo nombre choca con otra categoría.
* `DELETE /categorias/{id}` — elimina una categoría; 204 si tuvo éxito,
  404 si no existe.

Todos los endpoints usan `get_db()` de `app/db/session.py` (Etapa 2) como
única vía de acceso a la base de datos; no hay lógica de conexión en las
rutas.

## Migración

* Archivo: `alembic/versions/9a974154a336_crear_tabla_categorias.py`.
* Generada con `alembic revision --autogenerate`, comparando contra una
  base PostgreSQL real, y luego ajustada a mano para agregar la carga de
  datos.
* El `upgrade()` crea la tabla `categorias` y carga las 8 categorías
  iniciales mediante `op.bulk_insert`. El `downgrade()` elimina la tabla
  (y por lo tanto también los datos).
* Se probó el ciclo completo `upgrade` → `downgrade` → `upgrade` contra
  PostgreSQL real, confirmando que es reversible y reproducible.
* `alembic/env.py` se actualizó para importar `Categoria`, de forma que
  `autogenerate` la detecte. Los modelos de etapas futuras deberán
  importarse de la misma manera.

## 8 categorías iniciales cargadas

1. Gastronomía
2. Alojamiento
3. Turismo
4. Comercios
5. Servicios
6. Salud y bienestar
7. Transporte
8. Eventos

Nombres y descripciones cargados exactamente como fueron definidos por
Jeff para VIVÍ SMA (no se modificaron ni se completaron con contenido
inventado).

## Estructura / archivos creados o modificados

**Creados:**
* `app/models/categoria.py`
* `app/schemas/categoria.py` (+ `app/schemas/__init__.py`)
* `app/routers/categorias.py` (+ `app/routers/__init__.py`)
* `alembic/versions/9a974154a336_crear_tabla_categorias.py`

**Modificados (solo agregados, sin borrar nada existente):**
* `app/main.py` — se agregó el import y `include_router` del router de
  categorías, y se actualizó el docstring superior para reflejar que
  Categoria ya no es un módulo pendiente. El endpoint `GET /` y el
  `GET /health/db` de etapas anteriores quedaron intactos.
* `alembic/env.py` — se agregó el import del modelo `Categoria` para que
  `autogenerate` lo detecte.
* `README.md` — se documentaron los nuevos endpoints, el paso de
  `alembic upgrade head` y la nueva estructura de carpetas.

## Decisiones arquitectónicas tomadas

* Separación de responsabilidades en cuatro capas, tal como pedía el
  prompt de la etapa: modelos (`app/models/`), esquemas
  (`app/schemas/`), rutas (`app/routers/`) y base de datos (`app/db/`,
  de la Etapa 2). No se agregó una capa adicional de "servicios" o
  "CRUD": la lógica de consulta vive directamente en las funciones de
  ruta, por simplicidad y para evitar sobreingeniería en una entidad tan
  simple.
* La carga de las 8 categorías iniciales se resolvió como parte de la
  migración de Alembic (`op.bulk_insert` dentro del `upgrade()`), en vez
  de un script de seed separado o una carga en el arranque de la app.
  Esto asegura que los datos iniciales viajen versionados junto con el
  esquema y se repliquen igual en cualquier entorno donde se corran las
  migraciones.
* `PUT /categorias/{id}` se implementó como reemplazo completo (requiere
  `nombre` y `descripcion` siempre), no como actualización parcial. Un
  `PATCH` para actualización parcial no fue pedido y no se agregó.
* Manejo de duplicados: un intento de crear o renombrar una categoría a
  un `nombre` ya existente devuelve `409 Conflict` en vez de un error 500
  genérico de base de datos.

## Regla permanente

Esta actualización deja registrada conceptualmente la Etapa 3 en el
Prompt Master, sin incluir código completo, conforme a la regla
permanente de documentación establecida.

---

## MODIFICACIÓN POSTERIOR — INTRODUCCIÓN DE CAPA DE SERVICE

Tras la implementación inicial de la Etapa 3, se incorporó una capa de
**service** para la entidad Categoria, cambiando el flujo arquitectónico
de `Router → SQLAlchemy → PostgreSQL` a:

```
Router → Service → SQLAlchemy → PostgreSQL
```

### Qué se incorporó

* Nuevo paquete `app/services/` con `__init__.py` y
  `categoria_service.py`.
* Toda la lógica de operaciones sobre categorías (listar, obtener, crear,
  actualizar, eliminar) se movió desde `app/routers/categorias.py` hacia
  `app/services/categoria_service.py`. El service es quien ejecuta las
  consultas SQLAlchemy, hace commit/rollback y detecta condiciones como
  "categoría no encontrada" o "nombre duplicado".
* El router quedó reducido a: recibir la request, invocar la función del
  service correspondiente, y traducir el resultado (o la excepción) a la
  respuesta HTTP (código de estado + detail). Ya no contiene consultas ni
  lógica de negocio propia.
* El service señala los casos de error mediante dos excepciones propias
  (`CategoriaNoEncontrada`, `NombreDuplicado`) en vez de lanzar
  `HTTPException` directamente, para que `app/services/` no dependa de
  FastAPI. El router captura esas excepciones y arma la misma respuesta
  HTTP que ya devolvía antes de este cambio (404 / 409 con los mismos
  mensajes).

### Qué NO cambió

* Modelos (`app/models/categoria.py`), esquemas
  (`app/schemas/categoria.py`), datos cargados, dependencias,
  configuración, migraciones y frontend: sin modificaciones.
* Comportamiento observable de la API: mismos endpoints, mismos códigos
  de estado, mismos mensajes de error, mismo formato de respuesta.
  Verificado con pruebas de regresión completas contra PostgreSQL real
  después del cambio.

### Decisión arquitectónica tomada

* Se usaron excepciones propias del dominio en el service en lugar de
  `HTTPException`, para mantener esa capa desacoplada de FastAPI. Es la
  única decisión de diseño necesaria para trasladar la lógica sin alterar
  el comportamiento externo de la API.

