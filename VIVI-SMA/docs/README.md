# VIVÍ SMA — Frontend v1.1 (separado y organizado)

> Este documento explica la reorganización técnica realizada sobre el **FRONTEND BASE v1.0** (ver `AUDITORIA_FRONTEND_BASE.md`). Es exclusivamente una separación de archivos: **mismo diseño, mismo contenido, mismo comportamiento**. No se rediseñó ni se agregó ninguna funcionalidad.

---

## 1. Qué cambió y qué no

**No cambió:** identidad visual, paleta de colores, tipografías, estructura de secciones, contenido, datos mock, animaciones (fade-up, stagger, parallax del hero, respiración de la franja, ANDI), comportamiento responsive, navegación.

**Sí cambió:** la organización técnica interna. Antes todo vivía en un único archivo `index.html` de 654 KB con HTML+CSS+JS+15 imágenes en base64 mezclados. Ahora es una estructura de carpetas con responsabilidades separadas, `index.html` pesa 10.5 KB, y las imágenes son archivos reales.

---

## 2. Estructura final

```
VIVI-SMA/
├── index.html              → Únicamente estructura y contenido HTML
├── css/
│   ├── variables.css       → :root, paleta de colores, sombras, bordes
│   ├── base.css            → Reset, tipografía global, utilidades (fondos, wrap, foco), layout compartido de secciones
│   ├── navigation.css      → Header, logo, links, hamburguesa, menú mobile
│   ├── hero.css             → Hero, buscador, ANDI, pills de intención
│   ├── components.css      → Tarjetas de negocio, categorías, badges, tags
│   ├── sections.css        → Franja fotográfica, Destacados, Promociones, Eventos, Footer
│   ├── responsive.css      → Ajustes de tablet (700px) y desktop (1000px)
│   └── motion.css          → Sistema de animaciones: reveal/stagger, keyframes, prefers-reduced-motion
├── js/
│   ├── data.js              → Los 5 arrays mock (categorías, negocios, destacados, promos, eventos)
│   ├── render.js            → Funciones que inyectan las tarjetas en el DOM a partir de data.js
│   └── ui.js                → Menú mobile, IntersectionObserver (reveal), parallax del hero
├── assets/
│   └── images/              → Las 10 imágenes reales extraídas del base64 original
├── docs/
│   ├── PROMPT_MASTER_VIVISMA.md      → Documento maestro vigente (fuente de verdad de producto/diseño)
│   ├── AUDITORIA_FRONTEND_BASE.md    → Auditoría del frontend base v1.0
│   └── README.md                     → Este documento
└── _archive/
    ├── index_lite.html      → Copia liviana sin imágenes (uso auxiliar, no es el proyecto)
    └── *_b64.txt             → Artefactos de codificación de imágenes, ya no necesarios
```

---

## 3. Responsabilidad de cada carpeta

- **`css/`** — Un archivo por responsabilidad, no por sección. Los media queries de tablet/desktop se agruparon en `responsive.css` (así ya estaban organizados en el archivo original) para no duplicar contexto entre archivos; el resto de cada archivo contiene su comportamiento base (mobile-first).
- **`js/`** — `data.js` es la única fuente de contenido (equivalente mock de lo que después serán tablas `businesses`, `categories`, `promotions`, `events` en el backend). `render.js` no sabe nada de datos, solo sabe pintar. `ui.js` es interacción pura (menú, scroll, animaciones), no toca datos.
- **`assets/images/`** — Nombres descriptivos (`logo-casa-del-ahumado.jpg`, `hero-vista-aerea-lago.webp`, etc.) en vez de hashes o nombres genéricos, para que sea legible en el próximo paso (migración a `/public/images/` en Next.js).
- **`docs/`** — Todo el historial de decisiones de producto y diseño, más esta documentación técnica.
- **`_archive/`** — Nada de esto es necesario para ejecutar el sitio. Se conserva por las dudas, pero es candidato a eliminarse definitivamente en la próxima etapa.

---

## 4. Qué se extrajo (imágenes Base64 → archivos reales)

| Archivo nuevo | Usado en |
|---|---|
| `hero-vista-aerea-lago.webp` | Fondo del Hero |
| `franja-costanera-lago.jpg` | Franja fotográfica "Patagonia Argentina" |
| `logo-casa-del-ahumado.jpg` | Descubrí + Destacados |
| `logo-cerveceria-del-bosque.jpg` | Descubrí + Destacados + Promoción |
| `logo-refugio-quila.jpg` | Descubrí |
| `logo-andes-bike-rental.jpg` | Descubrí + Promoción |
| `logo-mercado-regional-patagonia.jpg` | Descubrí |
| `logo-estudio-wellness-andes.jpg` | Descubrí + Promoción |
| `logo-cabanas-lago-azul.jpg` | Destacados |
| `logo-sabores-del-cerro.jpg` | Destacados |

Las 15 apariciones originales (algunos negocios se repiten en más de una sección) se resolvieron correctamente a estas 10 imágenes únicas — se verificó que ninguna quedó rota y que todas conservan exactamente el mismo contenido visual, sin pérdida de calidad (se decodificó el base64 original byte a byte, no se volvió a comprimir).

---

## 5. Limpieza técnica realizada

- **Función `IMG()` eliminada.** Estaba definida pero sin ningún uso real (quedó de la etapa de placeholders, antes de las fotos reales). Se confirmó con un chequeo de 0 referencias antes de borrarla.
- **Ningún otro código fue eliminado.** El resto del comportamiento, clases CSS y estructura HTML se conservó exactamente igual.

---

## 6. Verificación realizada

✅ HTML, CSS y JavaScript separados sin pérdida: se comparó automáticamente que los **247 selectores CSS** del archivo original están presentes, íntegros y sin duplicar en los 8 archivos nuevos (diff exacto, cero diferencias). El JavaScript se validó con `node --check` tanto en cada archivo por separado como concatenado en el orden real de carga.

✅ Todas las rutas de `<link>`, `<script src>` e imágenes fueron verificadas contra el disco — las 13 rutas referenciadas existen físicamente.

✅ Balance de etiquetas HTML (`div`, `section`, `header`, `footer`, `nav`, `head`, `body`) verificado en 1:1.

⚠️ **Limitación honesta de esta verificación:** este entorno de trabajo no tiene un navegador gráfico disponible, por lo que no se pudo abrir `index.html` en un navegador real y observarlo visualmente, ni revisar la consola de DevTools en vivo. La verificación realizada es estática (integridad sintáctica y de referencias) y no reemplaza una prueba visual manual. **Recomendación:** al recibir el proyecto, abrí `index.html` haciendo doble clic y confirmá visualmente que el Hero, la navegación, las tarjetas, ANDI y las animaciones se vean y comporten igual que en la versión anterior.

---

## 7. Cómo ejecutar el proyecto localmente

No requiere instalación ni build. Dos formas:

**Opción A — Abrir directamente:**
Doble clic en `index.html`. Al usar rutas relativas (`css/...`, `js/...`, `assets/...`) en vez de imágenes embebidas, funciona igual abriendo el archivo directamente desde el sistema de archivos (`file://`).

**Opción B — Servidor local simple (recomendado para evitar restricciones del navegador con `file://`):**
```bash
cd VIVI-SMA
python3 -m http.server 8000
```
Y abrir `http://localhost:8000` en el navegador.

---

## 8. Qué queda pendiente (no se hizo en esta etapa, a propósito)

- Migración a componentes de React/Next.js (etapa posterior).
- Conexión a backend/PostgreSQL — los datos siguen siendo 100% mock en `js/data.js`.
- Eliminación definitiva de `_archive/` (se conserva por precaución en esta entrega).
- No se instaló ningún framework, bundler ni dependencia nueva — sigue siendo HTML/CSS/JS vanilla, tal como pedía el alcance de esta etapa.

---

**Este paquete reemplaza al FRONTEND BASE v1.0 como referencia de trabajo, bajo el nombre VIVÍ SMA — Frontend v1.1.**
