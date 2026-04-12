# Food Delivery (Django)

## Project Overview

This project is a Django-based web application where a static HTML/CSS template has been successfully integrated into the Django framework. The goal was to understand how to convert a static frontend design into a dynamic Django project structure.

---

## Features Implemented

- Integrated HTML/CSS template into Django
- Setup of static files (CSS, JS, images)
- Template rendering using Django views
- Base template structure for reusability
- Basic project routing using URLs

---

## Tech Stack

- Python
- Django
- HTML5
- CSS3
- Bootstrap (if used in template)

---

## Project Structure

```
memorial_project/
│
├── home/                # Django app
├── memorial_project/   # Project settings
├── static/             # Static files (CSS, JS, images, libs)
├── templates/          # HTML templates
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
```

2. Navigate to project directory:

```
cd memorial_project
```

3. Install dependencies:

```
pip install django
```

4. Run migrations:

```
python manage.py migrate
```

5. Start development server:

```
python manage.py runserver
```

6. Open in browser:

```
http://127.0.0.1:8000/
```

## What I Learned

- How Django handles templates and static files
- Converting static UI into reusable Django templates
- Project structuring in Django
- Importance of base templates and template inheritance

## Future Improvements

- Add database integration
- Implement user authentication
- Make pages dynamic
- Add forms and backend logic

## Acknowledgment

Frontend template was sourced from an open online resource and adapted into Django for learning purposes.
