# 🍲 Zavor App — Plataforma Gastronómica de Villa El Salvador

> **Zavor** es una plataforma web y móvil concebida para visibilizar, digitalizar y conectar a los comensales con los mejores huariques, pollerías, cebicherías y restaurantes locales de **Villa El Salvador (VES)** sin intermediarios ni comisiones abusivas.

---

## 📌 Tabla de Contenidos
1. [Características Principales](#-características-principales)
2. [Alineación con las ODS (ONU Agenda 2030)](#-alineación-con-las-ods-onu-agenda-2030)
3. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
4. [Requisitos Previos](#-requisitos-previos)
5. [Instalación y Configuración Paso a Paso](#-instalación-y-configuración-paso-a-paso)
6. [Estructura del Proyecto](#-estructura-del-proyecto)
7. [Créditos y Equipo Fundador](#-créditos-y-equipo-fundador)
8. [Licencia](#-licencia)

---

## ✨ Características Principales
- 🚀 **Landing Page Moderna:** Diseño optimizado, responsivo y de alto contraste gastronómico.
- 📱 **Descarga Directa de APK:** Descarga directa e instantánea del instalador Android de Zavor (`ZavorApp-v1.0-VillaElSalvador.apk`).
- 📍 **Mapa e Identificación Local:** Selección inteligente de huariques por sector y categoría en VES.
- 🍲 **MYPEs al 0% Comisiones:** Soporte 100% gratuito para pequeños emprendedores gastronómicos.
- 🤝 **Impacto Social:** Proyecto de innovación social desarrollado por estudiantes de Ingeniería de Sistemas de la UNTELS.

---

## 🌍 Alineación con las ODS (ONU Agenda 2030)
- **ODS 8 | Trabajo Decente y Crecimiento Económico:** Digitalización de MYPEs gastronómicas locales.
- **ODS 9 | Industria, Innovación e Infraestructura:** Democratización de herramientas tecnológicas y geolocalización.
- **ODS 11 | Ciudades y Comunidades Sostenibles:** Impulso al comercio y consumo de proximidad.

---

## 🛠️ Tecnologías Utilizadas
- **Backend:** Python 3.10+ & Django 4.2
- **Frontend:** HTML5, Vanilla CSS3 (Custom Design System), JavaScript (ES6+)
- **Íconos & Tipografía:** FontAwesome 6 Pro, Google Fonts (Outfit & Plus Jakarta Sans)
- **Servidor WGI / Despliegue:** Gunicorn & Django StaticFiles

---

## 📋 Requisitos Previos

Asegúrate de tener instalado en tu sistema:
- **Python 3.10+**: [Descargar Python](https://www.python.org/downloads/)
- **Git**: [Descargar Git](https://git-scm.com/)
- **pip** (Administrador de paquetes de Python)

---

## ⚙️ Instalación y Configuración Paso a Paso

### 1️⃣ Clonar el Repositorio
Abre tu terminal (PowerShell, Bash o WSL) y ejecuta:
```bash
git clone https://github.com/Alfaro33-stack/zavor_web.git
cd zavor_web
```

### 2️⃣ Crear y Activar un Entorno Virtual (Venv)

**En Linux / WSL / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Instalar las Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4️⃣ Ejecutar las Migraciones de Django
```bash
python manage.py migrate
```

### 5️⃣ Iniciar el Servidor de Desarrollo
```bash
python manage.py runserver
```

Abre tu navegador e ingresa a: **`http://127.0.0.1:8000/`** 🚀

---

## 📁 Estructura del Proyecto

```text
zavor_web/
├── db.sqlite3                 # Base de datos local SQLite
├── manage.py                  # CLI de gestión de Django
├── requirements.txt            # Dependencias del proyecto
├── README.md                  # Guía principal del proyecto en GitHub
├── zavor_web/                 # Configuración principal de Django
│   ├── settings.py            # Ajustes, apps e imágenes estáticas
│   ├── urls.py                # Rutas globales
│   └── wsgi.py                # Entrada WSGI para producción
└── landing/                   # App principal de la Landing Page
    ├── apps.py                # Configuración de la App Landing
    ├── views.py               # Vistas principales (Home y descarga APK)
    ├── urls.py                # Enrutador interno de la landing
    ├── static/                # Archivos estáticos
    │   ├── apk/               # Instalador APK Android
    │   ├── css/               # Estilos globales y diseño
    │   └── images/            # Logos, fotografías de fundadores y platos
    └── templates/             # Plantillas HTML
        └── landing/
            └── index.html     # Landing Page principal
```

---

## 👥 Créditos y Equipo Fundador

- **José Luis Alfaro** — *Co-Fundador & Estrategia de Producto / Ingeniería*  
  - 🔗 [LinkedIn](https://www.linkedin.com/in/jose-luis-alfaro-mendoza-71b59a3a2/) | [Facebook](https://www.facebook.com/profile.php?id=61585653447183) | [Instagram](https://www.instagram.com/alfaromendozajoseluis3/) | [GitHub](https://github.com/Alfaro33-stack)
- **Jostink Hernandez** — *Co-Fundador & Dev Lead / Ingeniería*  
  - 🎓 *Estudiantes de 8vo Ciclo de Ingeniería de Sistemas (UNTELS)*

---

## 📄 Licencia
Este proyecto es una iniciativa de desarrollo e ingeniería social sustentada por la comunidad estudiantil de la **UNTELS (Universidad Nacional Tecnológica de Lima Sur)**.
