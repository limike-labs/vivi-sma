# models/

Carpeta preparada para los futuros modelos SQLAlchemy de VIVÍ SMA
(usuarios, negocios, categorías, eventos, etc.).

En la Etapa 2 se deja intencionalmente vacía (además del `__init__.py`
requerido para que sea un paquete Python), ya que el diseño definitivo de
las entidades corresponde a etapas posteriores.

Cuando se agreguen modelos, deben heredar de `app.db.session.Base` para
que Alembic pueda detectarlos vía autogenerate.
