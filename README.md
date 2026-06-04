# Subestaciones Eléctricas México - Grupo CGE

Este proyecto es una Landing Page moderna, de alto impacto visual y orientada a la conversión, diseñada para la empresa **Grupo CGE (Subestaciones Eléctricas)**. El objetivo principal de la página es destacar la experiencia técnica de la empresa, generar confianza a través de certificaciones y logotipos de clientes, y capturar clientes potenciales (leads) mediante un formulario de contacto y llamadas a la acción (CTAs) estratégicamente ubicados.

## Tecnologías Utilizadas

El proyecto está construido priorizando el rendimiento, la accesibilidad y un diseño moderno (Bento Grid, Glassmorphism, animaciones suaves) utilizando tecnologías web estándar y herramientas de construcción modernas:

- **HTML5:** Estructura semántica.
- **CSS3 (Vanilla):** Estilos personalizados, variables CSS, Flexbox, CSS Grid (para el layout Bento Box), y animaciones (keyframes para la cinta de clientes). No se utilizan frameworks CSS pesados.
- **JavaScript (Vanilla):** Lógica de animaciones al hacer scroll (Intersection Observer), validación de formularios y comportamiento de la barra de navegación.
- **Vite:** Herramienta de compilación (build tool) y servidor de desarrollo local. Proporciona recarga en caliente (HMR) ultrarrápida y compilación optimizada para producción.

## Estructura del Proyecto

```text
/
├── public/                 # Archivos estáticos (imágenes, logos, favicons) que se copian directamente a /dist.
│   ├── images/             # Imágenes generadas de alta calidad (4k) para fondos y beneficios.
│   ├── favicon.svg         # Ícono del sitio.
│   └── ...                 # Logos de clientes (Benavides, Oxxo, etc.)
├── index.html              # Archivo HTML principal. Contiene toda la estructura de la landing page.
├── style.css               # Hoja de estilos principal. Incluye variables de tema oscuro y cyan corporativo.
├── main.js                 # Lógica interactiva (scroll, animaciones, formulario).
├── package.json            # Dependencias del proyecto y scripts de Node.js.
├── vite.config.js          # Configuración del servidor Vite (si aplica).
└── README.md               # Este archivo de documentación.
```

## Guía de Instalación y Desarrollo Local

Para trabajar en este proyecto de manera local, asegúrate de tener instalado [Node.js](https://nodejs.org/) (versión 16+ recomendada).

1. **Instalar dependencias:**
   Ejecuta el siguiente comando en la raíz del proyecto para descargar las herramientas necesarias:
   ```bash
   npm install
   ```

2. **Iniciar el servidor de desarrollo:**
   Para visualizar la página en tu navegador con recarga automática cada vez que guardes un cambio en el código:
   ```bash
   npm run dev
   ```
   Esto levantará un servidor local (usualmente en `http://localhost:5173`).

3. **Construir para Producción:**
   Una vez que hayas terminado de realizar cambios y quieras desplegar el sitio, debes construir la versión optimizada:
   ```bash
   npm run build
   ```
   Este comando generará una carpeta `dist/` que contendrá el código HTML, CSS y JS minificado y listo para ser alojado en cualquier servidor web estático (Vercel, Netlify, AWS S3, Hostinger, etc.).

4. **Previsualizar la versión de producción (Opcional):**
   ```bash
   npm run preview
   ```

## Características Clave del Código

- **Bento Grid:** La sección de "Beneficios" (Ventajas) está construida utilizando un layout asimétrico de CSS Grid (`.bento-grid`), lo que le da un aspecto muy premium y moderno.
- **Efectos de Scroll:** Los elementos aparecen dinámicamente a medida que el usuario hace scroll hacia abajo. Esto se controla en `main.js` usando el API de `IntersectionObserver` y las clases `.scroll-trigger` de CSS.
- **Cinta de Logos Infinita:** La franja de marcas (`.marquee`) está implementada con CSS puro (`@keyframes marquee`) y un truco de duplicación de contenido en HTML para asegurar un ciclo infinito (seamless loop) incluso en monitores ultra-anchos.
- **Tema Oscuro y Acentos:** La paleta de colores se gestiona mediante variables CSS nativas (`:root`), predominando el azul oscuro naval con acentos en cian (`#00C2E8`).

## Mantenimiento Futuro

- **Cambio de Imágenes:** Para cambiar una imagen, simplemente reemplaza el archivo en la carpeta `public/` o actualiza la ruta `src=""` dentro de `index.html`. 
- **Información de Contacto:** Todos los datos (teléfono, dirección, email, enlaces) se encuentran en texto plano dentro del archivo `index.html` (principalmente en el `<header>` y en el `<footer>`), por lo que son fáciles de actualizar.
- **Nuevos Estilos:** Todo nuevo componente debe ser estilizado en `style.css` respetando las variables de color globales para mantener la coherencia visual.
