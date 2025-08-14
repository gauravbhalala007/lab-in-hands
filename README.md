# Lab In Hands

**Lab In Hands** is a Django-based web application designed to provide patients and healthcare professionals with easy online access to medical reports, along with a responsive, mobile-friendly interface and the foundation for future report visualization.

This project was developed as part of my **Bachelor’s thesis** and serves as a starting point for a full-featured hospital/clinic reporting portal.

---

## Features

- **Responsive Medical-Themed UI**  
  - Landing page, About, Doctors, Contact, and Login pages.
  - Built with Bootstrap 4, animations, and reusable components.

- **Structured Django Project**  
  - Clear separation of templates, static assets, and application logic.
  - Routing structure ready for expansion into authenticated workflows.

- **Static Asset Pipeline**  
  - Organized `static/` directory for CSS, JS, and images.
  - Configured `STATICFILES_DIRS` and `STATIC_ROOT` for production builds.

- **Future-Ready Backend**  
  - Prepared for integration with patient data models, medical report uploads, and graph-based data visualizations.

---

## Project Structure
lab-in-hands/
├── lab_in_hands/ # Project configuration (settings, URLs, WSGI)
├── admin/ # Custom Django app (views, URLs, templates)
├── templates/ # HTML templates for pages
├── static/ # CSS, JS, images, and PHP mail handler
├── assets/ # Static files build output (collectstatic)
├── db.sqlite3 # SQLite database (currently minimal)
├── manage.py # Django management script
└── README.md # Project documentation

---

## Tech Stack

- **Backend:** Django 2.2, Python 3.x, SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 4, JavaScript
- **Template Engine:** Django Templates
- **Static Assets:** Managed via Django staticfiles

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lab-in-hands.git
   cd lab-in-hands

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate     # On macOS/Linux
    venv\\Scripts\\activate        # On Windows

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt


4. **Apply migrations**
    ```bash
    python manage.py migrate

5. **Run the development server**
    ```bash
    python manage.py runserver

6. **Access the app**
   Open your browser and go to:
   ```bash
   http://127.0.0.1:8000/

