import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Favicon
content = content.replace(
    '<link rel="icon" type="image/svg+xml" href="/vite.svg" />',
    '<link rel="icon" type="image/png" href="/logo_subestaciones_bco.png" />'
)

# 2. Extract hero-icons and remove from hero
hero_icons_regex = re.compile(r'\s*<div class="hero-icons animate-up delay-1">.*?</div>\n', re.DOTALL)
match = hero_icons_regex.search(content)
if match:
    hero_icons_html = match.group(0)
    # Remove animate-up and delay-1 from the extracted html for the banner
    hero_icons_banner = hero_icons_html.replace('hero-icons animate-up delay-1', 'hero-icons')
    content = content.replace(match.group(0), '')

# Fix delays in hero
content = content.replace('class="hero-subtitle animate-up delay-2"', 'class="hero-subtitle animate-up delay-1"')
content = content.replace('class="hero-buttons animate-up delay-3"', 'class="hero-buttons animate-up delay-2"')

# 3. Extract trust banner and replace with icon-banner and install-section
trust_banner_regex = re.compile(r'\s*<!-- Cinta de Autoridad -->\s*<section class="trust-banner">.*?</section>\n', re.DOTALL)
match = trust_banner_regex.search(content)
if match:
    trust_banner_html = match.group(0)
    
    new_sections = f"""
    <!-- Icon Banner -->
    <section class="icon-banner">
      <div class="container">
{hero_icons_banner}
      </div>
    </section>

    <!-- Installation Info Section -->
    <section class="installation-section">
      <div class="container">
        <h2 class="section-title text-light scroll-trigger">Instalación de subestaciones eléctricas y transformadores</h2>
        <div class="install-grid">
          <div class="install-card scroll-trigger slide-in-left">
            <div class="install-card-header">
              <h3>Servicio de suministro e instalación</h3>
            </div>
            <div class="install-card-body">
              <ul>
                <li>Análisis de la necesidad en capacidad en KVA y tipo de subestación eléctrica</li>
                <li>Incluimos el proceso de tramites con CFE, SENER y CENACE</li>
                <li>Suministro e instalación de la subestación eléctrica</li>
                <li>Peritaje y valoración por la unidad verificadora de instalaciones eléctricas UVIE ó SEMIP</li>
                <li>Realizamos la interconexión con la red de CFE y la contratación del servicio</li>
              </ul>
            </div>
          </div>
          <div class="install-card scroll-trigger slide-in-right delay-1">
            <div class="install-card-header">
              <h3>Mantenimiento</h3>
            </div>
            <div class="install-card-body">
              <ul>
                <li>Somos la empresa #1 en Mantenimiento a Subestaciones Eléctricas de cualquier capacidad, desde 15KVA hasta 7,000 KVA.</li>
                <li>Ofrecemos servicio gratuito de Consultoría y Asesoría.</li>
                <li>Brindamos mantenimiento a Subestaciones Eléctricas y revisamos el flujo de energía.</li>
                <li>Brindamos revisión, limpieza de componentes y reparamos las piezas necesarias.</li>
                <li>Hacemos pruebas eléctricas y de funcionamiento.</li>
                <li>Contamos con equipos de alta tecnología y personal certificado</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
"""
    content = content.replace(match.group(0), new_sections)

# 4. Re-insert trust banner below timeline
# Find timeline end: </section>\n\n    <!-- Footer & Form -->
timeline_end_regex = re.compile(r'    </section>\n\n    <!-- Footer & Form -->')
match = timeline_end_regex.search(content)
if match:
    insert_str = "    </section>\n\n" + trust_banner_html + "\n    <!-- Footer & Form -->"
    content = content.replace(match.group(0), insert_str)

with open('index.html', 'w') as f:
    f.write(content)

print("HTML update script complete.")
