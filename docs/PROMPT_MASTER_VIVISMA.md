# VIVÍ SMA — PROMPT MAESTRO DE CONSTRUCCIÓN

> Este documento es el Prompt Master vigente de VIVÍ SMA. Contiene el documento original (secciones 1-44) sin modificar, más las directivas estratégicas incorporadas posteriormente (secciones 45-48). No se elimina ni reescribe ninguna instrucción anterior.

---

# 1. ROL

Actuá como un desarrollador senior full-stack, especialista en UX/UI, arquitectura web, frontend moderno y desarrollo de productos digitales escalables.

Vas a construir VIVISMA siguiendo estrictamente la identidad, arquitectura, experiencia de usuario y decisiones funcionales descritas en este documento.

No improvises cambios importantes de arquitectura, identidad visual o experiencia de usuario.

Cuando exista una decisión que pueda afectar significativamente el proyecto, explicala antes de modificarla.

---

# 2. PRODUCTO

## Nombre

**VIVISMA** (marca visual: **VIVÍ SMA**)

## Claim

**Todo San Martín de los Andes en un solo lugar**

## Concepto

VIVISMA es una plataforma digital independiente de descubrimiento local para San Martín de los Andes.

Su objetivo es permitir que residentes y turistas puedan descubrir: dónde comer, dónde dormir, qué hacer, qué comprar, qué servicios existen, qué eventos ocurren, promociones, negocios locales, actividades, experiencias.

VIVISMA NO debe sentirse como un directorio tradicional. Debe sentirse como una experiencia digital para descubrir San Martín de los Andes.

---

# 3. PERSONALIDAD DE MARCA

**Natural · Fresca · Moderna · Profesional · Viva**

### Natural
La interfaz debe transmitir naturaleza y Patagonia sin caer en clichés. No llenar la página de montañas, hojas, árboles o símbolos turísticos. La naturaleza debe sentirse mediante: colores, fotografías, espacios, composición, texturas sutiles, sensación de amplitud.

### Fresca
Ligera, limpia y agradable. Evitar exceso de elementos, sombras, bordes, saturación de colores, interfaces pesadas.

### Moderna
Tarjetas modernas, bordes suaves, microinteracciones, animaciones sutiles, navegación clara, responsive design, excelente experiencia móvil.

### Profesional
Debe transmitir confianza. Producto digital profesional y preparado para crecer.

### Viva
Transmitir movimiento y descubrimiento mediante fotografías, animaciones y transiciones, sin volverse una interfaz exageradamente animada.

---

# 4. IDENTIDAD VISUAL (ORIGINAL)

> Nota: esta paleta fue reemplazada por la Nueva Identidad Cromática (sección 45). Se conserva aquí como registro histórico de la decisión original.

Verde VIVISMA #176B4D · Verde profundo #0D3B2E · Crema #F7F4EA · Blanco #FFFFFF · Negro #111111 · Gris oscuro #4B514E · Naranja #E8792F · Celeste #8CCFD1.

---

# 5. REGLA DE COLOR (ORIGINAL)

El verde es la identidad de VIVISMA. Los demás colores son complementarios. Prioridad: 1) Verde 2) Crema/blanco 3) Negro/gris 4) Naranja 5) Celeste. (Ver sección 45 para la regla de color vigente.)

---

# 6. TIPOGRAFÍA

## Titulares: DM Serif Display
Grandes títulos, frases de impacto, encabezados de sección editoriales.

## Interfaz y textos: Manrope
Navegación, botones, buscadores, tarjetas, formularios, descripciones, textos generales.

---

# 7. PRINCIPIO DE DISEÑO

VIVISMA debe respirar: espacios amplios, márgenes generosos, jerarquía clara, fotografías grandes, bloques visuales diferenciados. El espacio vacío forma parte de la identidad.

---

# 8. HOMEPAGE — HERO

VIVISMA centrado, protagonista visual. Orden: VIVISMA → claim → buscador (placeholder "¿Qué estás buscando?") → "¿QUÉ QUERÉS HACER?" (🍽️ Comer, 🏔️ Hacer, 🛏️ Dormir, 🛍️ Comprar, 🔧 Servicios, 📅 Eventos).

---

# 9. HERO VISUAL

Fotografías auténticas de San Martín de los Andes. Overlays sutiles para legibilidad. Evitar bancos de imágenes genéricos si hay alternativas auténticas.

---

# 10. NAVEGACIÓN

Minimalista. Mínimo: VIVISMA, Explorar, Categorías, Destacados, Promociones, Eventos, buscador, acceso cuando exista autenticación. Menú limpio en móvil.

---

# 11. SECCIÓN "DESCUBRÍ"

"Descubrí lugares cerca tuyo". Tarjetas con: fotografía, nombre, categoría, valoración, ubicación, etiquetas, estado Destacado.

---

# 12. TARJETAS

Bordes suavemente redondeados, sombras muy sutiles, buena separación, imágenes protagonistas, tipografía clara, jerarquía visual. Hover: transición leve, zoom ligero, elevación sutil. Sin animaciones exageradas.

---

# 13. DESTACADOS

"🔥 Destacados en VIVISMA" (ver sección 47/48: sin ícono de fuego, badge naranja/terracota). Negocios pagos identificados como "DESTACADO". Pagar no implica mejores reseñas — publicidad y recomendación mantienen separación conceptual.

---

# 14. CATEGORÍAS

"Explorá San Martín": Gastronomía, Alojamiento, Turismo y actividades, Comercios, Servicios, Salud y bienestar, Transporte, Eventos. Ampliable a futuro.

---

# 15. "¿QUÉ QUERÉS HACER?"

Diferencial de VIVISMA: el usuario expresa una intención en lenguaje natural. Inicialmente filtros y lógica básica; posteriormente IA (ver sección 46, ANDI).

---

# 16. PROMOCIONES

Sección "Promociones" con acento naranja (ver sección 45: acento Sol Patagónico). Mostrar negocio, promoción, imagen, vigencia, categoría, botón. Nunca agresiva.

---

# 17. EVENTOS

Nombre, fecha, horario, ubicación, imagen, descripción, categoría, negocio/organizador.

---

# 18. FICHA DINÁMICA DEL NEGOCIO

NO crear una página HTML por negocio. Plantilla dinámica, ej. `/negocio/la-montana`, renderizada desde base de datos.

---

# 19. ESTRUCTURA DE LA FICHA

Foto principal, logo, nombre, categoría, valoración, descripción, galería, dirección, horario, WhatsApp, Instagram, sitio web, menú/catálogo, servicios, promociones, reseñas, mapa, cómo llegar, reserva/contacto.

---

# 20. PERSONALIZACIÓN DEL NEGOCIO

Logo, fotografías, colores, contenido, promociones — siempre dentro de la identidad general de VIVISMA.

---

# 21. RESEÑAS

Sistema de reseñas separado de la publicidad. Pagar no mejora la puntuación. Sin manipulación artificial.

---

# 22. MODELO DE NEGOCIO

Freemium: Plan Gratuito (presencia profesional básica), Plan Destacado (visibilidad, promociones, estadísticas), Plan Premium (exposición avanzada, campañas). Precios a definir.

---

# 23. PANEL ADMINISTRADOR

Ruta `/admin`, autenticación segura. Dashboard, negocios, categorías, usuarios, reseñas, promociones, eventos, suscripciones, destacados, estadísticas, configuración.

---

# 24. PANEL DEL COMERCIANTE

Ruta `/mi-negocio` (ver sección 47 para la evolución completa a Panel Profesional). Edición exclusiva del propio negocio, con permisos que impiden acceso cruzado.

---

# 25. BASE DE DATOS

PostgreSQL. Modelo conceptual: businesses, categories, subcategories, users, photos, reviews, promotions, events, subscriptions, business_settings, business_services. Pensada para escalar sin duplicación innecesaria.

---

# 26. STACK TECNOLÓGICO

Frontend: React/Next.js. Backend: Python + FastAPI. Database: PostgreSQL. Repositorio: GitHub. Editor: VS Code.

---

# 27. RESPONSIVE DESIGN

Mobile first. Funcional en teléfonos, tablets, notebooks, desktops. Botones fáciles de tocar. Acciones clave accesibles (WhatsApp, ubicación, cómo llegar, contacto, reserva).

---

# 28. ANIMACIONES (ORIGINAL)

Microanimaciones: aparición progresiva, hover de tarjetas, transición de botones, zoom ligero, desplazamiento suave, navegación fluida. La animación aporta vida, no distrae. (Ver sección 48 para el sistema de motion design ampliado.)

---

# 29. ACCESIBILIDAD

Contraste suficiente, textos legibles, navegación por teclado, etiquetas accesibles, alt text, botones identificables, foco visible.

---

# 30. SEO

URLs amigables, títulos dinámicos, meta descriptions, Open Graph, sitemap, robots.txt, datos estructurados. Fichas de negocio posicionables individualmente.

---

# 31. ARQUITECTURA

Separar: Frontend, Backend, Database, Authentication, Components, Pages, Services, Utilities, Assets. Código modular, sin archivos gigantes.

---

# 32. CALIDAD DEL CÓDIGO

Código limpio, componentes reutilizables, nombres claros, separación de responsabilidades, seguridad, validación, manejo de errores, variables de entorno, documentación básica. Sin datos sensibles hardcodeados.

---

# 33. GITHUB

Repositorio oficial VIVISMA. Control de versiones. Commits claros (`Initial project structure`, `Create homepage hero`, `Add business cards`, `Create business detail page`, `Add category system`). Versionado progresivo.

---

# 34. VS CODE

Entorno local de desarrollo. Debe poder ejecutarse localmente antes de desplegar.

---

# 35. DESARROLLO POR VERSIONES — V0.1

Homepage, identidad VIVISMA, hero, buscador visual, categorías, tarjetas, destacados, "¿Qué querés hacer?", ficha dinámica de negocio, responsive. Datos mock. Sin funciones complejas todavía.

**Estado actual: V0.1 en curso — frontend visual completo con mock data, sin backend.**

---

# 36. V0.2

Backend, PostgreSQL, negocios reales, categorías dinámicas, administración básica.

---

# 37. V0.3

Autenticación, panel administrador, panel comerciante, reseñas, promociones.

---

# 38. V0.4

Planes, suscripciones, estadísticas, monetización.

---

# 39. V0.5+

Recomendaciones inteligentes, IA (ver ANDI, sección 46), "¿Qué querés hacer?" con IA real, PWA, notificaciones, automatizaciones, reservas, nuevas herramientas para comercios.

---

# 40. PRINCIPIO DE DESARROLLO

No construir todo de una vez. Por etapas: **experiencia → estructura → MVP → validación → funcionalidades → monetización → automatización → IA**.

---

# 41. DATOS INICIALES

Negocios ficticios marcados como demostración durante el desarrollo. Al incorporar negocios reales: nombre, categoría, descripción, dirección, teléfono, WhatsApp, Instagram, web, horarios, fotografías, logo, servicios, menú, promociones, ubicación, plan.

---

# 42. PRINCIPIOS ABSOLUTOS DE VIVISMA

1. VIVISMA es una experiencia, no un directorio.
2. El verde es la identidad *(actualizado por sección 45: el terracota pasa a ser el color protagonista; el verde queda en segundo plano)*.
3. Natural · Fresca · Moderna · Profesional · Viva.
4. El diseño debe respirar.
5. Mobile-first.
6. La publicidad nunca destruye la credibilidad.
7. Las reseñas no se compran.
8. Los negocios gratuitos tienen presencia digna y profesional.
9. Los planes pagos ofrecen visibilidad y herramientas.
10. Las recomendaciones priorizan relevancia y utilidad.
11. Primero construir manualmente y validar. Después automatizar.
12. (continúa en 11)
13. La arquitectura debe permitir crecer.
14. No crear páginas individuales manualmente para cada negocio.
15. Utilizar componentes reutilizables.
16. Mantener identidad visual consistente.
17. No sobrecargar la interfaz con animaciones.
18. No utilizar colores sin función.
19. Priorizar velocidad y experiencia de usuario.
20. Construir VIVISMA como un producto real y escalable.

---

# 43. OBJETIVO FINAL

**"La forma más fácil y agradable de descubrir qué hacer, dónde ir y qué encontrar en San Martín de los Andes."** No solo una web: una plataforma local. **VIVÍ SMA — Todo San Martín de los Andes en un solo lugar.**

---

# 44. INSTRUCCIÓN FINAL PARA LA IMPLEMENTACIÓN

Antes de escribir código: analizar el documento, proponer estructura técnica, crear arquitectura de carpetas, explicar decisiones importantes, crear la primera versión funcional, mantener la identidad visual, no cambiar el concepto sin justificar, construir modular, preparar para GitHub, no implementar funcionalidades futuras fuera de la etapa actual.

**La prioridad absoluta de V0.1 es crear una experiencia visual excelente, rápida, responsive y coherente con la identidad de VIVISMA.**

---
---

# DIRECTIVAS ESTRATÉGICAS INCORPORADAS

> A partir de aquí, nuevas directivas oficiales y permanentes del ecosistema VIVÍ SMA, integradas sin reemplazar lo anterior. Ante cualquier conflicto entre una implementación nueva y la estructura ya construida, prevalece la conservación del proyecto existente y la solución menos invasiva.

---

# 45. IDENTIDAD CROMÁTICA DE VIVÍ SMA

VIVÍ SMA tiene una identidad visual propia, viva, cálida, moderna, minimalista y claramente diferenciada de Pulse SMA.

**Paleta oficial vigente — paleta original de VIVÍ SMA (fuente de verdad)** *(revisión 5; ver historial de cambios más abajo)*:

- **Verde VIVÍ SMA — #176B4D**: color principal de identidad. Naturaleza, bosque, Patagonia, confianza. Uno de los colores principales de toda la interfaz — botones, navegación activa, categorías, detalles de interacción.
- **Verde Profundo — #0D3B2E**: color de profundidad. Fondos oscuros, footer, overlays de fotografía, elementos de alto contraste.
- **Crema — #F7F4EA**: color cálido principal. Fondos, superficies, secciones claras.
- **Blanco — #FFFFFF**: tarjetas, superficies, textos sobre fondos oscuros, elementos limpios.
- **Negro — #111111**: títulos, textos principales, máximo contraste.
- **Gris oscuro — #4B514E**: textos secundarios, metadata, información complementaria.
- **Naranja — #E8792F** *(sin cambios desde la versión inicial, color reservado y exclusivo)*: acento. Badge DESTACADO, llamadas de atención. No debe eliminarse ni sustituirse.
- **Celeste — #8CCFD1**: color secundario de la identidad. Detalles, acentos, variaciones visuales, componentes donde el sistema lo indique (p. ej. Eventos, Promociones) — sin convertirlo en color dominante.

**Regla de proporción:** la identidad se construye principalmente con Verde + Verde Profundo + Crema + Blanco, usando Naranja + Celeste como colores secundarios/acento. Que existan varios colores en la paleta no significa usarlos todos simultáneamente en todas las secciones — paleta rica pero controlada, no interfaz multicolor.

**Regla del Hero:** la fotografía es el elemento protagonista desde el primer momento, nunca un bloque verde sólido. El overlay usa Verde Profundo (`#0D3B2E`) semitransparente sobre la foto para legibilidad y profundidad, sin teñirla por completo ni saturarla.

**Degradados:** solo a partir de la paleta oficial o transparencias de esos colores (verde → transparencia, verde profundo → transparencia, combinaciones sutiles entre verdes). Nunca degradados multicolor ni colores ajenos a la identidad.

**Reglas de aplicación:** conservar estructura, layout, componentes, funcionalidades, textos, tipografías, tamaños, espaciados y animaciones existentes. No agregar ni quitar elementos por esta directiva. Verificar en desktop, tablet y mobile: contraste correcto, legibilidad, botones con suficiente contraste, estados hover/active claros, ausencia de colores residuales de identidades anteriores.

**Estado de implementación:** aplicado sobre el frontend V0.1 actual (ver registro de cambios al final de este documento).

**Historial de revisiones de esta directiva:**
1. *Versión inicial:* Terracota (#E56B4A) como color protagonista, Verde Bosque secundario, Sol Patagónico (#F2B84B) como acento, Arena (#F4EBDD), Grafito (#252525), Blanco Cálido (#FFFDFC).
2. *Ajuste Arena Patagonia:* el tono Arena se corrigió de `#F4EBDD` a `#E8DFCF` por su matiz cremoso-violáceo.
3. *Revisión "Cuatro Estaciones":* se revierte el protagonismo al Verde Bosque, el terracota pasa a rol secundario con tono otoñal (#C96A4A), se incorporan Verde Profundo, Verde Salvia, Blanco Nieve, Crema Luz Patagónica, Arena Sol y Dorado Sol.
4. *Revisión "Bosque · Nieve/Aire · Luz · Montaña":* se reduce la cantidad de colores protagonistas. El terracota, el celeste y el arena/salvia dejan de usarse como protagonistas. Verde VIVÍ SMA (#1F6B50) y Verde Profundo (#123C32) consolidan el hilo conductor; se incorporan Amarillo Solar (#E4B84A) y Dorado Suave (#D5B66A) como acentos de luz muy moderados.
5. *Restauración de la paleta original (vigente):* se recupera exactamente la paleta original definida en la sección 4 del documento fundacional — Verde `#176B4D`, Verde Profundo `#0D3B2E`, Crema `#F7F4EA`, Blanco `#FFFFFF`, Negro `#111111`, Gris `#4B514E`, Naranja `#E8792F` y **Celeste `#8CCFD1`** (que había quedado sin uso activo en las revisiones 3 y 4, y ahora vuelve a aplicarse como color secundario en Eventos y Promociones). Esta paleta original queda establecida como fuente de verdad: cualquier ajuste cromático futuro debe partir de ella, no de las paletas alternativas exploradas en las revisiones 1 a 4. El Naranja Destacados (#E8792F) se mantiene exactamente igual en las cinco versiones.

---

# 46. ANDI — LA MONTAÑITA VIAJERA DE VIVÍ SMA

ANDI es el asistente inteligente y personaje visual oficial de VIVÍ SMA: una pequeña montaña viajera que representa naturaleza + aventura + descubrimiento + cercanía + calidez.

VIVÍ SMA = la plataforma. ANDI = su guía inteligente y personaje.

**Función:** ayudar a encontrar lugares, actividades, eventos, promociones, servicios, experiencias y recomendaciones, sintiéndose como un compañero de descubrimiento, no un chatbot corporativo.

**Personalidad:** simpático, curioso, aventurero, cálido, inteligente, servicial, expresivo, cercano, positivo, moderno. Tierno pero con estética moderna, limpia y premium — nunca frío ni excesivamente infantil.

**Apariencia:** pequeña montaña/personaje con silueta propia y reconocible, ojos expresivos, expresión amable, pequeño pañuelo/bufanda, bastón de trekking o elemento de aventura, estética limpia y moderna. No debe ser un simple logo de montaña.

**Interacción por lenguaje natural** (conceptual en esta etapa, con mock data): preguntas del tipo "¿Dónde puedo comer algo rico esta noche?", "¿Qué puedo hacer hoy?". En fase frontend/prototipo: mock data, respuestas simuladas, arquitectura preparada para integración futura. NO IA real, backend real, base de datos real ni reservas reales todavía.

**Presencia en el Hero:** integrado visualmente junto al buscador ("Preguntale a Andi"), con reacciones sutiles a foco/escritura/búsqueda.

**Viaje por la página:** puede acompañar el scroll con estados: IDLE, WALKING, THINKING, DISCOVERING, POINTING, HAPPY, EXPLORING, RESTING, GREETING, ERROR/NO RESULTS (siempre amable, nunca haciendo sentir mal al usuario).

**Ubicación visual posible (no simultánea, con lógica narrativa):** Hero, Buscador, Categorías, "¿Qué hacer hoy?" (sección conceptualmente ligada a "¿Qué querés hacer?", sección 15), Promociones, Eventos, Actividades, Recomendaciones, Footer. La sensación debe ser la de ANDI viajando y descubriendo el contenido junto al usuario, no la de un ícono fijo repetido en todos lados a la vez.

**Reglas no negociables:** respeta la identidad visual y paleta oficial (sección 45); responsive (más libre en desktop, compacto en mobile); nunca tapa contenido, botones ni navegación; nunca es obligatorio para usar la plataforma; respeta `prefers-reduced-motion` (minimizar animación, conservar presencia visual y función).

**Arquitectura futura (conceptual):** AndiUI, AndiSearch, AndiRecommendations, AndiAnimation, AndiCharacter, AndiData — separación preparada para conectar con backend real más adelante, sin implementarse todavía.

**Estado de implementación:** incorporado como personaje visual estático/idle en el Hero (SVG propio), sin lógica conversacional real (etapa de prototipo).

---

# 47. PANEL PROFESIONAL PARA NEGOCIOS

VIVÍ SMA evoluciona de directorio a plataforma de valor medible para comercios: **VISIBILIDAD + HERRAMIENTAS + DATOS + OPORTUNIDADES COMERCIALES**, no solo presencia.

**Panel del negocio (conceptual):** administración de nombre, logo, descripción, fotos, categoría, dirección, horarios, teléfono, WhatsApp, redes, ubicación, servicios/productos.

**Analíticas (prioridad estratégica futura):** visitas (día/semana/mes, comparativas), interacciones (WhatsApp, teléfono, cómo llegar, Instagram, web, reservas, promociones), origen del descubrimiento (búsqueda, categoría, home, promoción, evento, recomendación, externo).

**Dashboard visual:** simple de interpretar (ejemplo mock: visitas, clicks en WhatsApp, solicitudes de ubicación, llamadas, visitas a promociones, guardados; rendimiento semanal; actividad por día). Todos los números de ejemplo son mock, nunca datos reales.

**Promociones:** creación (título, descripción, imagen, precios, descuento, fechas, horarios, condiciones, cupos, código, botón de contacto/reserva) y control (activas/próximas/finalizadas, visualizaciones, clicks, contactos, rendimiento).

**Leads y medición:** embudo explícito **VISITA → INTERACCIÓN → CONTACTO → RESERVA → VENTA**, cada etapa medida por separado. Nunca afirmar conversión a venta sin poder comprobarla.

**Favoritos, posicionamiento y publicaciones:** guardados, veces compartido, apariciones en búsquedas/categorías — nunca datos engañosos ni métricas inventadas.

**Eventos del negocio:** creación con métricas independientes (visualizaciones, clicks, contactos, reservas).

**Notificaciones al comerciante:** ejemplos conceptuales de alertas de rendimiento y vencimientos, como herramienta de retención.

**Centro de recomendaciones (futuro, con IA):** sugerencias accionables basadas en datos. NO IA real todavía en fase de prototipo — solo interfaz preparada.

**Modelo de monetización futuro:** Gratuito, Pro, Destacado, Promocionado, Premium. Sin precios definitivos aún — primero validar producto y valor generado.

**Separación arquitectónica conceptual:** Usuario (descubrir, buscar, guardar, contactar, reservar, valorar) / Negocio (administrar, publicar, promocionar, medir) / Administración VIVÍ SMA (gestionar negocios, moderar, categorías, planes, métricas globales).

**Estado de implementación: NO implementado en el frontend actual.** Requiere backend, autenticación y base de datos reales — queda como directiva vigente para la etapa V0.2/V0.3 en adelante, según el orden ya definido en las secciones 36-39.

---

# 48. SISTEMA DE ANIMACIONES Y MOTION DESIGN

Capa de motion design sutil y premium sobre la interfaz existente, sin rediseñar estructura, contenido, paleta, tipografías, tamaños, espaciados, navegación ni componentes.

**Hero:** parallax muy suave (el fondo se desplaza a velocidad ligeramente distinta al scroll). Pequeño, estable, sin mareo. No altera altura ni composición.

**Cards:** fade-up + stagger al entrar en viewport (opacity 0 + leve desplazamiento hacia posición final, con pequeño retraso entre tarjetas consecutivas). Se ejecuta una sola vez, no se repite al salir del viewport. Sin rebotes.

**Títulos y subtítulos:** slide-up + fade, rápido y elegante.

**Imágenes:** reveal progresivo + pequeño desplazamiento vertical, sin alterar proporciones ni tamaño ni generar cambios permanentes de layout.

**Botones:** fade + scale muy sutil (sin overshoot ni elasticidad).

**Transiciones de color entre secciones:** degradados amplios y suaves usando exclusivamente la paleta oficial (sección 45) — variaciones de tonalidad/saturación, nunca colores nuevos. Sensación de evolución continua, no de corte entre secciones.

**Legibilidad:** verificar contraste de títulos, texto, botones, cards e iconos durante toda transición. El fondo nunca compite con el contenido.

**Coordinación:** todas las técnicas (hero, cards, títulos, imágenes, botones, fondos) deben sentirse como una sola experiencia fluida, no como efectos independientes.

**Prioridad:** elegancia > suavidad > naturalidad > rapidez > rendimiento. Sin rebotes, movimientos bruscos, zooms fuertes, parallax excesivo ni efectos que distraigan.

**Responsive:** valores adaptados por dispositivo; en mobile reducir o desactivar efectos que afecten rendimiento, batería o experiencia táctil.

**Accesibilidad:** todas las animaciones (incluidas las de ANDI) respetan `prefers-reduced-motion` — se reducen o eliminan sin perder función ni presencia visual esencial.

**Rendimiento:** priorizar propiedades animables eficientemente (`transform`, `opacity`), evitar layout thrashing y dependencias innecesarias. Evaluar reutilización antes de instalar librerías nuevas.

**Estado de implementación:** sistema base de fade-up/reveal (IntersectionObserver, una sola ejecución), parallax sutil de hero, variante fade+scale para botones/links de acción (`.reveal-btn`, reutiliza el mismo observer) y franjas de transición de color entre secciones (CSS puro, sin JS, solo colores ya existentes en la paleta) incorporados sobre el frontend V0.1 actual, en JavaScript vanilla, sin dependencias nuevas.

---

# REGLA ABSOLUTA SOBRE EL PROYECTO ACTUAL

Si alguna directiva puede interpretarse como motivo para rediseñar innecesariamente la interfaz existente, prevalece: **conservar la estructura actual y evolucionarla, no reemplazarla.** No hacer refactors innecesarios. No cambiar contenido. No alterar funcionalidades existentes. No instalar dependencias innecesarias. No implementar backend, autenticación, base de datos, pagos, reservas o IA real mientras estemos en fase de prototipo/frontend.

**Metodología vigente:** ANALIZAR → INTEGRAR → ESTRUCTURAR → VISUALIZAR → MOCKEAR → VERIFICAR.
