# VIVÍ SMA — AUDITORÍA FRONTEND BASE v1.0

> Documento de auditoría, congelamiento y línea base del frontend actual de VIVÍ SMA, previo al diseño de arquitectura de backend. No se modificó ningún aspecto de diseño, contenido ni funcionalidad durante esta auditoría — es un trabajo exclusivamente de inspección, prueba, respaldo y documentación.

---

## A. RESUMEN EJECUTIVO

VIVÍ SMA cuenta hoy con **un frontend estático, autocontenido en un único archivo** (`index.html`), sin backend, sin base de datos y sin build system. Es HTML5 + CSS3 + JavaScript vanilla, con datos de negocios/categorías/promociones/eventos hardcodeados como arrays JS (mock data) y 15 imágenes reales incrustadas como `base64` directamente en el documento.

El archivo pesa 654 KB (de los cuales ~430 KB son las imágenes en base64; el HTML+CSS+JS "puro" ronda los 220 KB). No se encontraron errores de sintaxis en HTML, CSS ni JavaScript. No existía repositorio Git antes de esta auditoría — se inicializó uno y se realizó el commit de congelamiento (ver sección L).

**Veredicto general: el frontend está en buen estado, es funcional, no tiene errores críticos, y es una base sólida y coherente para diseñar el backend.**

---

## B. STACK TECNOLÓGICO

| Capa | Tecnología | Versión / detalle |
|---|---|---|
| Estructura | HTML5 | Un único archivo (`index.html`), 1200 líneas |
| Estilos | CSS3 puro | Sin preprocesador, sin framework (no Tailwind, no Bootstrap). Variables CSS nativas (`:root`) para el sistema de diseño |
| Comportamiento | JavaScript vanilla (ES6+) | Sin librerías, sin frameworks (no React, no Vue). Usa `IntersectionObserver`, `matchMedia`, template literals, arrow functions |
| Tipografía | Google Fonts (CDN) | DM Serif Display + Manrope, cargadas vía `<link>` — **única dependencia externa real** |
| Build system | **No existe** | No hay `package.json`, `vite.config`, `webpack.config` ni ningún bundler. Se abre el `.html` directamente en el navegador |
| Gestor de paquetes | **No existe** | Cero dependencias npm/yarn |
| Backend | **No existe** | Confirmado — no hay ninguna llamada a API, `fetch()`, ni servidor |
| Base de datos | **No existe** | Confirmado |
| Control de versiones | **No existía antes de esta auditoría.** Se inicializó Git y se hizo el commit baseline (ver sección L) |

---

## C. ESTRUCTURA DEL PROYECTO

No hay carpetas — todo el proyecto vive en un directorio plano:

```
vivisma/
├── index.html                  ← EL PROYECTO REAL (frontend completo)
├── PROMPT_MASTER_VIVISMA.md    ← Documento maestro vigente (fuente de verdad de decisiones de producto/diseño)
├── index_lite.html             ← Copia derivada SIN imágenes embebidas (creada a pedido, para pegar en otro chat de IA; NO es el proyecto)
├── ahumado_logo_b64.txt        ← Artefacto de codificación (scratch)
├── bike_logo_b64.txt           ← Artefacto de codificación (scratch)
├── cabanas_logo_b64.txt        ← Artefacto de codificación (scratch)
├── cerveceria_logo_b64.txt     ← Artefacto de codificación (scratch)
├── franja_b64.txt              ← Artefacto de codificación (scratch)
├── hero_b64.txt                ← Artefacto de codificación (scratch)
├── lagosma_b64.txt             ← Artefacto de codificación (scratch, no usado en el HTML final)
├── mercado_logo_b64.txt        ← Artefacto de codificación (scratch)
├── refugio_logo_b64.txt        ← Artefacto de codificación (scratch)
├── sabores_logo_b64.txt        ← Artefacto de codificación (scratch)
└── wellness_logo_b64.txt       ← Artefacto de codificación (scratch)
```

**Dentro de `index.html`, la organización interna es:**

```
<head>                    líneas 1-10    → meta tags, título, fuentes
<style>                   líneas 11-823  → ~812 líneas de CSS (sistema de diseño completo)
<body>                    líneas 825-1023 → estructura HTML (nav, hero, secciones, footer)
<script>                  líneas 1024-1198 → mock data + lógica de render + interacciones
```

**Componentes visuales identificados dentro del CSS/HTML** (no son componentes de framework, son bloques de HTML+CSS repetidos por convención de nombre de clase):
`.nav`, `.hero` / `.hero-photo` / `.hero-float`, `.andi-avatar` (personaje ANDI), `.searchbar`, `.intent-row` (pills "¿Qué querés hacer?"), `.card` (tarjeta de negocio, reutilizada en Descubrí y Destacados), `.cat-card` (categoría), `.promo-card`, `.evento-card`, `.franja` (franja fotográfica editorial), `footer`.

**No existen:** carpetas `components/`, `pages/`, `services/`, `assets/` — la arquitectura de carpetas del documento maestro (sección 31) todavía no se implementó porque corresponde a la etapa de migración a React/Next.js, no a esta.

---

## D. FUNCIONALIDADES EXISTENTES

### FUNCIONALIDADES REALES (funcionan en el navegador tal cual)
- Navegación sticky con scroll suave a anclas internas (`#descubri`, `#categorias`, `#destacados`, `#promociones`, `#eventos`).
- Menú hamburguesa mobile funcional (abre/cierra, bloquea el scroll del body mientras está abierto, cierra al hacer click en un link).
- Nav responsive real: enlaces + botón CTA visibles solo en desktop (≥900px), hamburguesa solo en mobile (<700px), con una zona intermedia de transición.
- Buscador visual (input de texto) — captura foco pero **no ejecuta ninguna búsqueda real** (no hay lógica de filtrado conectada).
- Fila "¿Qué querés hacer?" con scroll horizontal táctil.
- Renderizado dinámico de tarjetas: negocios, categorías, destacados, promociones y eventos se generan en tiempo de carga desde arrays JS (`.map()` + `innerHTML`), no están hardcodeados en el HTML.
- Animación de aparición (fade-up + stagger) de títulos y tarjetas al hacer scroll, vía `IntersectionObserver`, ejecutada una sola vez por elemento.
- Parallax sutil del hero vinculado al scroll (`requestAnimationFrame`).
- Animación de "respiración" (aparece/permanece/desaparece en loop) en el texto de la franja fotográfica.
- Personaje ANDI (SVG propio) con animación idle.
- Franjas de transición de color entre secciones (CSS puro, sin JS).
- Soporte completo de `prefers-reduced-motion`: todas las animaciones tienen su contraparte estática.

### FUNCIONALIDADES SIMULADAS (mock data)
- **5 arrays JavaScript hardcodeados** en el `<script>`: `categorias` (8 ítems), `negocios` (6 ítems), `destacados` (4 ítems), `promos` (3 ítems), `eventos` (4 ítems).
- Las 15 fotos de negocios/logos están **incrustadas como base64**, no vienen de ningún storage ni CDN propio.
- El aviso visible "Datos de demostración" ya está en el HTML, dejando explícito ante el usuario que el contenido es ficticio.

### FUNCIONALIDADES INCOMPLETAS O DECORATIVAS (preparadas visualmente, sin backend detrás)
- Botón "Buscar" del hero: no dispara ninguna acción real.
- Botón "Sumá tu negocio" (nav + footer): `href="#"`, sin destino.
- Links "Ver todo" / "Ver todas" / "Ver agenda" (Descubrí, Destacados, Promociones, Eventos): `href="#"`, sin destino ni paginación real.
- Links de Instagram/WhatsApp del footer: `href="#"`, sin destino.
- En total hay **15 enlaces con `href="#"`** — todos son placeholders intencionales de esta etapa, no errores.
- No existe ficha individual de negocio (`/negocio/[slug]`) — las tarjetas no son clickeables hacia ningún detalle todavía (correctamente, según el documento maestro, eso corresponde a V0.2+).
- Función `IMG(seed, w, h)` (generador de URLs de picsum.photos): sigue **definida en el código pero sin ningún uso activo** — es código muerto que quedó de cuando las imágenes eran placeholders genéricos, antes de incrustar las fotos reales. No causa errores, pero es candidato a limpieza.

---

## E. DATOS

**No hay backend. No hay base de datos. No hay localStorage. No hay API.**

Todos los datos que ve el usuario provienen exclusivamente de **5 arrays de JavaScript definidos directamente en el `<script>` del propio `index.html`** (`categorias`, `negocios`, `destacados`, `promos`, `eventos`). Se recrean desde cero cada vez que se recarga la página — no hay ninguna persistencia entre sesiones ni entre pestañas.

Las imágenes no son archivos separados: son strings `base64` embebidos en el atributo `src` de cada `<img>`, dentro de esos mismos arrays.

---

## F. ESTADO VISUAL

Identidad vigente: paleta original de VIVÍ SMA restaurada como fuente de verdad (Verde `#176B4D`, Verde Profundo `#0D3B2E`, Crema `#F7F4EA`, Blanco `#FFFFFF`, Negro `#111111`, Gris `#4B514E`, Naranja `#E8792F` exclusivo de "Destacado", Celeste `#8CCFD1` como secundario). Tipografía DM Serif Display (títulos) + Manrope (interfaz). Estructura de homepage: Nav → Hero (foto + buscador + ANDI) → Descubrí → Categorías (bloque verde oscuro) → Franja fotográfica editorial → Destacados → Promociones → Eventos → Footer.

Sistema de motion design activo: fade-up/stagger, parallax de hero, animación de la franja, transiciones de color entre secciones — todo documentado en la sección 48 del Prompt Master.

---

## G. RESPONSIVE

**Breakpoints detectados en el código:** `700px`, `900px` (específico de la nav), `1000px`, más la media feature `prefers-reduced-motion`.

- **Desktop (≥1000px):** nav completa con los 5 links + botón CTA, grillas de 3-4 columnas en Destacados/Promociones/Eventos, tarjetas de Descubrí a ancho fijo (268px) en un carrusel.
- **Tablet (700-999px):** nav completa pero compacta, grillas de 2 columnas.
- **Mobile (<700px):** nav reducida a logo + búsqueda + hamburguesa, tarjetas de Descubrí al 40% del ancho de pantalla (carrusel con "peek"), Destacados en grilla de 2 columnas.

No se detectaron reglas CSS con `overflow` sin controlar ni anchos fijos en píxeles que pudieran generar overflow horizontal en pantallas chicas (se validó `body{overflow-x:hidden}` como red de seguridad adicional). No se pudo hacer una prueba real en un navegador/dispositivo físico (este entorno no tiene navegador gráfico disponible); el análisis es estático sobre el código y sobre el histórico de ajustes responsive ya realizados y confirmados en esta misma conversación en iteraciones previas.

---

## H. ERRORES ENCONTRADOS

### Críticos
**Ninguno.** El HTML, CSS y JavaScript son sintácticamente válidos (verificado con `node --check` sobre el JS extraído, y verificación de balance de etiquetas/llaves).

### Importantes
**Ninguno funcional.** No hay imports rotos, no hay imágenes con ruta inexistente (todas son base64 embebidas o Google Fonts vía CDN válido), no hay IDs duplicados, no hay anchors de navegación que apunten a un `id` inexistente.

### Menores
1. **Función `IMG()` sin uso** (código muerto) — quedó del sistema de placeholders inicial, antes de las fotos reales. No rompe nada, pero conviene eliminarla en una futura limpieza.
2. **15 enlaces `href="#"`** sin destino real — esperado y correcto para esta etapa, pero deben quedar en el radar para cuando se conecten a rutas reales (fichas de negocio, panel, redes sociales).
3. **Dependencia externa única:** Google Fonts vía CDN. Si no hay conexión a internet al abrir el archivo, el sitio sigue funcionando pero usa la tipografía de respaldo del sistema en vez de DM Serif Display/Manrope.
4. **Archivos sueltos no esenciales** (`*_b64.txt`, `index_lite.html`) conviviendo en la misma carpeta que el proyecto real — no afectan el funcionamiento pero conviene separarlos o eliminarlos antes de migrar a la estructura de carpetas definitiva.
5. **`lagosma_b64.txt`** es un artefacto de codificación de una imagen que finalmente no quedó en uso en el HTML actual (se reemplazó en una iteración posterior) — puede eliminarse sin impacto.

---

## I. ARQUITECTURA ACTUAL

```
Usuario
   ↓
Navegador (abre index.html directamente, sin servidor)
   ↓
HTML (estructura) + CSS (estilos, ya cargado inline en <style>)
   ↓
JavaScript vanilla (se ejecuta al cargar la página)
   ↓
Arrays hardcodeados en el propio <script>  ←  ESTO ES "LA BASE DE DATOS" HOY
   ↓
.map() + innerHTML → inyecta las tarjetas en el DOM
```

No hay capa de red, no hay estado persistente, no hay separación entre "frontend" y "backend" — es un documento único que se autocontiene y autorenderiza.

---

## J. PREPARACIÓN PARA BACKEND

### Lo que YA EXISTE y puede mapearse directamente
Los 5 arrays mock ya tienen una forma tabular consistente, muy cercana al modelo conceptual que el propio Prompt Master define en su sección 25:

| Array mock actual | Tabla conceptual ya definida en el Prompt Master |
|---|---|
| `negocios` / `destacados` | `businesses` |
| `categorias` | `categories` |
| `promos` | `promotions` |
| `eventos` | `events` |

Campos ya presentes en el mock que probablemente sean columnas reales: `nombre`, `cat` (categoría), `loc` (ubicación), `tags`, `destacado` (booleano), `img`. En promociones: `neg` (negocio asociado), `promo` (texto), `vig` (vigencia), `img`. En eventos: `dia`, `mes`, `nombre`, `hora`, `lugar`, `cat`.

### Lo que PROBABLEMENTE se necesitará (no decidido todavía, solo detectado como hueco funcional)
- Autenticación de usuarios (todavía no existe ningún concepto de sesión/usuario en el frontend).
- Endpoint de búsqueda real (el input ya existe visualmente, sin lógica).
- Rutas dinámicas de ficha de negocio (`/negocio/[slug]`), mencionadas en el Prompt Master sección 18 pero no implementadas aún en el frontend.
- Almacenamiento real de imágenes (hoy son base64 embebidas; un backend probablemente querrá URLs a un storage/CDN).
- Sistema de reseñas (mencionado en el Prompt Master sección 21, sin ningún rastro en el frontend actual — ni siquiera mock).
- Paneles `/admin` y `/mi-negocio` (Prompt Master secciones 23-24 y 47) — no existen ni como mock en el frontend hoy.

**Aclaración importante:** esta lista es un relevamiento de huecos funcionales visibles, no una decisión de alcance — eso queda para cuando definamos la arquitectura del backend.

---

## K. RIESGOS TÉCNICOS

1. **Peso del archivo (654 KB):** al migrar a React/Next.js, las 15 imágenes base64 deberán extraerse a archivos reales servidos como estáticos (`/public/images/`) — si se migran tal cual incrustadas, cada carga de página seguirá pesando lo mismo innecesariamente.
2. **Ausencia total de manejo de errores en JS:** no hay ningún `try/catch` ni verificación de que los elementos del DOM existan antes de operarlos (`document.getElementById('burgerBtn')` asume que el elemento siempre está presente). Funciona hoy porque el HTML es estático y controlado, pero es un patrón a fortalecer cuando haya renderizado dinámico real desde una API (los datos podrían no llegar, fallar, o tardar).
3. **Cero pruebas automatizadas** (ni unitarias ni end-to-end) — esperable en esta etapa, pero es una deuda a incorporar antes de escalar funcionalidades.
4. **No hay control de versiones histórico:** recién en esta auditoría se inicializó Git. Todo el historial de decisiones de diseño previas a este commit vive únicamente en la conversación, no en commits incrementales — al migrar a la estructura de carpetas definitiva, conviene recrear el historial de decisiones importantes en los mensajes de commit (el Prompt Master ya sugiere convenciones de nombre en su sección 33).
5. **Acoplamiento fuerte estilo-contenido-lógica:** al estar todo en un único archivo, cualquier cambio de datos requiere editar el mismo archivo que el diseño — no es un riesgo hoy (es la decisión correcta para esta etapa), pero es exactamente lo que la migración a componentes de React/Next.js debe resolver.

---

## L. GIT

- **Estado antes de la auditoría:** no existía repositorio Git en el proyecto.
- **Acción tomada:** se inicializó un repositorio nuevo (`git init`) en `/home/claude/vivisma`, ya que no había ningún historial previo que pudiera perderse — no hubo ningún riesgo de sobrescritura.
- **Branch:** `master` (por defecto).
- **Commit de congelamiento realizado:** ✅ Sí.
- **Mensaje:** `chore: freeze frontend baseline v1.0`
- **Archivos incluidos:** los 14 archivos existentes en el directorio (`index.html`, `PROMPT_MASTER_VIVISMA.md`, `index_lite.html`, y los 11 archivos `*_b64.txt`).
- **Working tree:** limpio, sin cambios pendientes después del commit.

---

## M. RECOMENDACIONES PARA LA SIGUIENTE ETAPA

*(Solo recomendaciones — nada de esto se implementó en esta auditoría.)*

1. Antes de migrar a React/Next.js, limpiar los archivos scratch (`*_b64.txt`, `index_lite.html`) o moverlos a una carpeta `_archive/` fuera del repo de trabajo.
2. Eliminar la función `IMG()` muerta al hacer la migración de componentes.
3. Extraer las 15 imágenes base64 a archivos reales en `/public/images/` durante la migración, en vez de mantenerlas incrustadas.
4. Diseñar el modelo de base de datos tomando como punto de partida los 5 arrays mock actuales (ya tienen forma tabular consistente) más las tablas ya previstas en la sección 25 del Prompt Master.
5. Definir qué `href="#"` se convierten en rutas reales primero (probablemente: ficha de negocio y búsqueda) versus cuáles esperan a una etapa posterior (panel de negocio, autenticación).
6. Incorporar manejo de errores básico en la capa de datos antes de conectar cualquier fetch real a una API.

---

**Esta versión queda establecida formalmente como VIVÍ SMA — FRONTEND BASE v1.0**, respaldada en el commit `chore: freeze frontend baseline v1.0` del repositorio Git recién inicializado.
