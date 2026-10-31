# 🎓 Student Management System

A simple web-based **Student Management System** developed using **Flask** and **SQLite**. This project was built to practice CRUD operations, Flask routing, database connectivity, and template rendering with Jinja2.

---

## 🚀 Features

* ➕ Register a new student
* 📋 View all student records
* 🔍 Search students using Roll Number
* ✏️ Update student information
* 🗑️ Delete student records
* 💬 Flash messages for user feedback
* 📱 Responsive and clean user interface

---

## 🛠️ Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Backend Programming    |
| Flask      | Web Framework          |
| SQLite     | Database               |
| HTML       | Page Structure         |
| CSS        | Styling                |
| JavaScript | Client-side Validation |
| Jinja2     | Dynamic Templates      |

---

## 📂 Project Structure

```text
Student_Management_System/
│
├── Database/
│   └── database.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── templates/
│   ├── layout.html
│   ├── dashboard.html
│   ├── register.html
│   ├── view.html
│   ├── update.html
│   └── search.html
│
├── app.py
├── database.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Madhavkris/Flask_Student_Management_System.git
```

Go to the project folder

```bash
cd Student_Management_System
```

Install Flask

```bash
pip install flask
```

Run the project

```bash
python app.py
```

Open your browser

```text
http://127.0.0.1:5000/
```

---

## 📸 Screenshots

### 🏠 Dashboard

![Home](screenshots/Home.png)

### ➕ Register Student

*![Register](screenshots/Register.png)

### 📋 View Students

![View](screenshots/View.png)

### 🔍 Search Student

![Search](screenshots/Search.png)

### 📋 Delete Student

![Delete](screenshots/Delete.png)


---

## 📚 What I Learned

During this project, I learned:

* Flask Routing
* CRUD Operations
* SQLite Database Integration
* Jinja2 Template Rendering
* Form Handling
* Flash Messages
* HTML, CSS & JavaScript Integration
* Project Structure in Flask

---

## 🔮 Future Improvements

* 🔐 Login Authentication
* 📄 Export Student Data
* 📊 Dashboard Statistics
* 🎨 Bootstrap UI
* ☁️ Deploy on Render

---

## 👨‍💻 Author

**Madhav Krishna**

B.Tech (ECE) Student

Learning Backend Development with Python & Flask


---

## ⚙️ CI/CD Pipeline (GitHub Actions)

This repository uses GitHub Actions to automatically validate changes pushed to the `main` branch and pull requests targeting `main`.

### Continuous Integration

The workflow is defined in `.github/workflows/ci.yml` and performs these steps:

1. Checks out the source code.
2. Sets up Python 3.10, 3.11, and 3.12 using a build matrix.
3. Installs dependencies from `requirements.txt`.
4. Runs automated tests with `pytest`.
5. Runs the Render deployment job only after the test matrix succeeds on pushes to `main`.

### Run tests locally

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

### Continuous Deployment (Render)

The repository includes a `Procfile` for running the Flask application with Gunicorn.

To enable automatic deployment:

1. Create a Web Service on [Render](https://render.com/) and connect this repository.
2. Use the build command: `pip install -r requirements.txt`.
3. Use the start command: `gunicorn app:app`.
4. In Render, create a Deploy Hook for the service.
5. In GitHub, open **Settings → Secrets and variables → Actions → New repository secret**.
6. Set the secret name to `RENDER_DEPLOY_HOOK` and paste the Deploy Hook URL as its value.

The workflow safely skips the deployment request until this secret is configured. Once configured, a successful push to `main` triggers Render deployment after all tests pass.

### Pipeline status

[![Flask CI/CD](https://github.com/vinil294/Flask_Student_Management_System/actions/workflows/ci.yml/badge.svg)](https://github.com/vinil294/Flask_Student_Management_System/actions/workflows/ci.yml)

