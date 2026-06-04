# Subestaciones Eléctricas México - Grupo CGE

Este proyecto es una Landing Page moderna, de alto impacto visual y orientada a la conversión, diseñada para la empresa **Grupo CGE (Subestaciones Eléctricas)**. El objetivo principal de la página es destacar la experiencia técnica de la empresa, generar confianza a través de certificaciones y logotipos de clientes, y capturar clientes potenciales (leads) mediante un formulario de contacto y llamadas a la acción (CTAs) estratégicamente ubicados.

## Tecnologías Utilizadas

El proyecto fue refactorizado y está construido bajo el ecosistema de **Astro**, priorizando el rendimiento, la accesibilidad, la arquitectura basada en componentes y un diseño moderno (Bento Grid, Glassmorphism, animaciones suaves):

- **Astro:** Framework web diseñado para velocidad, permitiendo la generación de sitios estáticos (SSG) de alta eficiencia con la filosofía de "Zero JS por defecto".
- **Componentes Astro (`.astro`):** Arquitectura modular (Header, Hero, Footer, etc.) que facilita el escalamiento y mantenimiento.
- **HTML5 & CSS3 (Vanilla):** Estructura semántica, variables CSS, Flexbox, CSS Grid (para el layout Bento Box), y animaciones (keyframes para la cinta de clientes). No se utilizan frameworks CSS pesados.
- **JavaScript (Vanilla):** Lógica de animaciones al hacer scroll (Intersection Observer) y comportamiento de la barra de navegación, aislada de manera eficiente dentro del layout base.

## Estructura del Proyecto

La nueva estructura de Astro distribuye lógicamente las responsabilidades:

```text
/
├── public/                 # Archivos estáticos (imágenes, logos, favicons) que Astro sirve tal cual a /dist.
│   ├── images/             # Imágenes optimizadas para fondos y beneficios.
│   ├── favicon.svg         # Ícono del sitio.
│   └── ...                 # Logos de clientes (Benavides, Oxxo, etc.)
├── src/                    # Código fuente del proyecto Astro.
│   ├── components/         # Módulos reutilizables de UI (Hero.astro, Benefits.astro, Footer.astro, etc.).
│   ├── layouts/            # Plantillas base (Layout.astro envuelve todas las páginas).
│   ├── pages/              # Rutas de la web (index.astro representa la página principal /).
│   ├── scripts/            # Lógica de JS global (main.js para el observer de scroll).
│   └── styles/             # Hojas de estilo globales (global.css).
├── package.json            # Dependencias del proyecto y scripts de Node.js.
├── astro.config.mjs        # Configuración de Astro (si aplica).
└── README.md               # Este archivo de documentación.
```

## Guía de Instalación y Desarrollo Local

Para trabajar en este proyecto de manera local, asegúrate de tener instalado [Node.js](https://nodejs.org/) (versión 18+ recomendada).

1. **Instalar dependencias:**
   Ejecuta el siguiente comando en la raíz del proyecto:
   ```bash
   npm install
   ```

2. **Iniciar el servidor de desarrollo:**
   Para previsualizar la página en tu navegador con Hot Module Replacement (HMR):
   ```bash
   npm run dev
   ```
   Esto levantará un servidor local rápido provisto por Astro.

3. **Construir para Producción:**
   Para compilar el sitio final ultrarrápido (Archivos estáticos HTML/CSS puros):
   ```bash
   npm run build
   ```
   Se generará la carpeta `dist/` lista para ser desplegada en Vercel, Netlify, AWS S3, Hostinger, etc.

4. **Previsualizar la versión de producción (Opcional):**
   ```bash
   npm run preview
   ```

## Características Clave del Código

- **Modularización Astro:** El código HTML gigante fue separado en múltiples componentes más pequeños (`src/components/`), facilitando que el equipo de desarrollo ubique y actualice fragmentos de código sin riesgo.
- **Formulario Actualizado:** El formulario de contacto ubicado en `Footer.astro` ha sido optimizado con un área de comentarios en vez de selectores limitantes.
- **Bento Grid:** La sección de "Beneficios" (Ventajas) está construida utilizando un layout asimétrico de CSS Grid (`.bento-grid`), dándole un aspecto muy premium.
- **Cinta de Logos Infinita:** Franja de marcas (`.marquee`) con CSS puro (`@keyframes marquee`) y contenido cíclico infinito.

## Mantenimiento Futuro

- **Imágenes Personalizadas y Optimizadas:** La imagen principal de portada (`public/images/hero_bg.jpg`) fue generada y editada mediante Inteligencia Artificial a una vista panorámica (16:9), limpiada de textos y severamente comprimida en JPEG (peso ~176KB) para mantener una excelente velocidad de carga.
- **Edición de Contenido:** Para cambiar textos o secciones, navega directamente al componente correspondiente en `src/components/`. 
- **Información de Contacto:** Todos los datos (teléfono, dirección, email, formulario) se encuentran en el archivo `src/components/Footer.astro`.
- **Nuevos Estilos:** Puedes estilizar cada componente directamente en su bloque `<style>` dentro del archivo `.astro`, o a nivel global en `src/styles/global.css`.
- **Scripts:** Si agregas interactividad a un componente de Astro, hazlo dentro de un tag `<script>` al final del archivo `.astro`. Astro lo procesará y optimizará automáticamente.
