# 🎓 Mini LMS (Learning Management System)

A full backend-driven Learning Management System built using **Django**, **Django REST Framework**, and **JWT Authentication**.

This project allows instructors to create courses and assignments, while students can view courses and submit assignments securely using token-based authentication.

---

# 📌 Table of Contents

- Project Overview
- Features
- Tech Stack
- System Architecture
- Database Models
- API Endpoints
- Role-Based Permissions
- Installation Guide
- Running the Project
- Future Improvements
- Author

---

# 📖 Project Overview

Mini LMS is a role-based learning management backend system designed to simulate real-world educational platforms.

It includes:

- Secure authentication using JWT
- Instructor and Student role management
- Course and assignment management
- Assignment submission system
- RESTful API architecture

This project is built for learning backend development and REST API design using Django.

---

# 🚀 Features

## 🔐 Authentication
- User Registration
- JWT Login (Access & Refresh Tokens)
- Secure API Access
- Role-Based Authorization

## 👨‍🏫 Instructor Capabilities
- Create Courses
- Create Assignments
- View Student Submissions
- Restricted access to instructor-only endpoints

## 👨‍🎓 Student Capabilities
- View Courses
- View Assignments
- Submit Assignments
- Restricted from creating courses/assignments

## 🌐 Frontend Pages
- Login Page
- Courses Page
- Assignments Page
- Dashboard (Basic UI)
- Styled using CSS

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3 | Programming Language |
| Django | Web Framework |
| Django REST Framework | API Development |
| SimpleJWT | Authentication |
| SQLite | Database |
| HTML & CSS | Frontend |
| Git & GitHub | Version Control |

---

# 🏗 System Architecture

```
Client (Frontend HTML/JS)
        ↓
Django REST API
        ↓
Database (SQLite)
```

Authentication Flow:

```
User Login → JWT Token Issued → Token Used in API Headers → Authorized Access
```

---

# 📂 Project Structure

```
backend/
│
├── backend/              # Project settings & configuration
│
├── accounts/             # Custom User & Authentication
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── courses/              # Course Management
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│
├── frontend/             # HTML & CSS files
│   ├── index.html
│   ├── dashboard.html
│   ├── courses.html
│   ├── assignments.html
│   ├── style.css
│
├── manage.py
└── db.sqlite3 (ignored in production)
```

---

# 🗄 Database Models

## 1️⃣ User (Custom User Model)
- email
- password
- role (Instructor / Student)
- is_staff
- is_active

## 2️⃣ Course
- title
- description
- instructor (ForeignKey → User)

## 3️⃣ Lesson
- title
- content
- course (ForeignKey → Course)

## 4️⃣ Assignment
- title
- description
- due_date
- course (ForeignKey → Course)

## 5️⃣ Submission
- assignment (ForeignKey)
- student (ForeignKey → User)
- content
- submitted_at

---

# 🔐 API Endpoints

## 🧑 Authentication

| Method | Endpoint | Description |
|--------|----------|------------|
| POST | /api/accounts/register/ | Register new user |
| POST | /api/token/ | Get JWT token |

---

## 📚 Courses

| Method | Endpoint | Access |
|--------|----------|--------|
| GET | /api/courses/courses/ | All users |
| POST | /api/courses/courses/ | Instructor only |

---

## 📝 Assignments

| Method | Endpoint | Access |
|--------|----------|--------|
| GET | /api/courses/assignments/ | All users |
| POST | /api/courses/assignments/ | Instructor only |

---

## 📤 Submissions

| Method | Endpoint | Access |
|--------|----------|--------|
| POST | /api/courses/submissions/ | Student only |

---

# 🛡 Role-Based Permissions

Custom permission classes ensure:

- Instructors can create courses & assignments
- Students cannot create courses
- Students can only submit assignments
- All endpoints require authentication

Example permission logic:

```python
if request.user.role == "instructor":
    allow_create_course()
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Ansh247452/mini-LMS.git
cd mini-LMS
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

---

## 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 🧪 Testing API with JWT

1. Login via:

```
POST /api/token/
```

2. Copy access token

3. Use in headers:

```
Authorization: Bearer your_access_token
```

---

# 🌟 Future Improvements

- Enrollment System
- Grading & Marks
- File Upload Support
- Dashboard Analytics
- Email Notifications
- Instructor Analytics
- Pagination
- Search & Filtering
- Deployment on Render / Railway / AWS
- PostgreSQL Migration
- Docker Containerization

---

# 🧠 Learning Outcomes

Through this project, concepts demonstrated:

- REST API Development
- Role-Based Authentication
- JWT Token System
- Model Relationships
- Permission Classes
- ViewSets & Routers
- Secure Backend Design

---

# 👨‍💻 Author

**Ansh247452**

GitHub:  
https://github.com/Ansh247452

---

# ⭐ Support

If you like this project, please ⭐ star the repository on GitHub.

---

# 📜 License

This project is built for educational purposes.
