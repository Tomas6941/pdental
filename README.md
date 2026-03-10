# 🦷 — Clínica Dental

Aplicación web para una clínica dental desarrollada con Python (Flask). Permite a los pacientes ver los servicios disponibles y reservar turnos online. Incluye un panel de administración para gestionar el contenido del sitio (No completado).

---

## 🛠️ Tecnologías utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

---

## ✨ Funcionalidades

- 🦷 Visualización de servicios ofrecidos por la clínica
- 📅 Reserva de turnos desde la web
- 🔐 Panel de administración para modificar títulos y contenido

---

## 📁 Estructura del proyecto

```
pdental/
├── app.py              # Servidor Flask y rutas
├── templates/
│   └── *.html          # Plantillas HTML (Jinja2)
└── static/
    ├── css/            # Estilos
    └── js/             # Scripts
```

---

## ⚙️ Cómo ejecutar

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/Tomas6941/pdental.git
   cd pdental
   ```
2. Creá un entorno virtual e instalá dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   pip install flask
   ```
3. Ejecutá la aplicación:
   ```bash
   python app.py
   ```
4. Abrí tu navegador en `http://localhost:5000`

---

## 👨‍💻 Autor

**Tomás** — [GitHub](https://github.com/Tomas6941)
