with open('style.css', 'r') as f:
    content = f.read()

new_css = """
/* Icon Banner */
.icon-banner {
  background-color: #0D1B2A;
  padding: 24px 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.icon-banner .hero-icons {
  margin-bottom: 0;
  justify-content: space-between;
}

@media (max-width: 768px) {
  .icon-banner .hero-icons {
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }
}

/* Installation Section */
.installation-section {
  background: linear-gradient(145deg, #0a192f 0%, #112240 100%);
  padding: 80px 0;
  color: var(--color-text-light);
}

.installation-section .section-title {
  color: var(--color-text-light);
  margin-bottom: 48px;
}

.install-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.install-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  transition: transform 0.3s ease;
}

.install-card:hover {
  transform: translateY(-5px);
  border-color: rgba(0, 194, 232, 0.3);
}

.install-card-header {
  background: rgba(0, 194, 232, 0.1);
  padding: 24px;
  border-bottom: 1px solid rgba(0, 194, 232, 0.2);
}

.install-card-header h3 {
  margin: 0;
  color: var(--color-brand-accent);
  font-size: 1.4rem;
}

.install-card-body {
  padding: 24px;
}

.install-card-body ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.install-card-body li {
  position: relative;
  padding-left: 28px;
  margin-bottom: 16px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
}

.install-card-body li:last-child {
  margin-bottom: 0;
}

.install-card-body li::before {
  content: "→";
  position: absolute;
  left: 0;
  top: 0;
  color: var(--color-brand-accent);
  font-weight: bold;
}

@media (max-width: 768px) {
  .install-grid {
    grid-template-columns: 1fr;
  }
}

"""

content = content.replace("/* Services */", new_css + "/* Services */")

with open('style.css', 'w') as f:
    f.write(content)

print("CSS update script complete.")
