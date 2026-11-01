# SmartHRM-An-Intelligent-Employee-Management-System

<div align="center">

[![Python Django](https://img.shields.io/badge/Backend-Django%20%2F%20DRF-green?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![React.js](https://img.shields.io/badge/Frontend-React.js-blue?style=for-the-badge&logo=react)](https://react.dev/)
[![YOLOv8 & FaceNet](https://img.shields.io/badge/AI%2FML-YOLOv8%20%2F%20FaceNet%20%2F%20OpenCV-orange?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-lightgrey?style=for-the-badge&logo=mysql)](https://www.mysql.com/)

*An enterprise-grade, AI-powered Human Resource Management platform featuring contactless biometric facial recognition attendance and predictive employee churn analytics.*

</div>

---

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Project Goals](#-project-goals)
- [Key Features & Architecture](#-key-features--architecture)
- [Technology Stack](#-technology-stack)
- [System Design & Diagrams](#-system-design--diagrams)
- [Project Structure & Database Schema](#-project-structure--database-schema)
- [Installation & Setup](#-installation--setup)
- [Project Team & Academic Context](#-project-team--academic-context)

---

## 🎯 About the Project

**SmartHRM** is a next-generation Human Resource Management System developed as an undergraduate Bachelor of Science (B.Sc.) thesis project in Computer Science and Engineering (CSE) at Dhaka International University. Traditional HR management systems rely heavily on manual record-keeping, vulnerable physical ID cards, or error-prone fingerprint scanners. SmartHRM solves these operational bottlenecks by combining a robust full-stack web platform with **computer vision** for automated biometric attendance and **machine learning** for predictive workforce analytics.

---

## 🎓 Project Goals

The primary goals of this project are:
1. **Centralized HR Operations:** Provide a unified digital workspace to seamlessly manage employee profiles, leave balances, expense claims, document repositories, and monthly payrolls[cite: 87].
2. **Eliminate Attendance Fraud:** Implement a secure, real-time, contactless biometric attendance pipeline utilizing device webcams, YOLOv8 face detection, and FaceNet facial embeddings[cite: 81].
3. **Proactive Workforce Management:** Build a machine learning module to evaluate workplace KPIs and predict employee attrition (churn risk) to help human resource teams intervene early with retention strategies[cite: 98].
4. **Role-Based Access Control (RBAC):** Secure sensitive administrative data using granular permission groups (Super Admin, HR Manager, Employees)[cite: 88, 98].

---

## 🚀 Key Features & Architecture

* **Contactless Biometric Attendance:** 
  * Captures live video feeds via device Webcam APIs[cite: 81].
  * Detects human faces instantaneously using **YOLOv8**[cite: 60].
  * Generates and compares facial embeddings using **FaceNet** and **OpenCV** to verify employee identity and log check-in/check-out timestamps automatically[cite: 61].
* **AI-Powered Churn Prediction:** Analyzes employee metrics such as age, satisfaction scores, overtime frequency, distance from home, and performance reviews to predict resignation risks[cite: 63, 64].
* **Comprehensive Core Modules:**
  * **Payroll Management:** Automated monthly salary calculations factoring in attendance records, bonuses, taxes, and leave deductions[cite: 97].
  * **Leave & Travel Management:** Streamlined workflow for applying, reviewing, and approving leaves and official business travel requests[cite: 96, 97].
  * **Document Repository:** Secure centralized document storage for appointment letters, employment contracts, and professional certificates[cite: 95].
* **Admin Dashboard & Audit Logs:** Real-time metrics overview accompanied by a chronological log of recent system actions for complete administrative transparency[cite: 88, 99].

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend** | React.js, Tailwind CSS, Bootstrap, JavaScript (ES6+)[cite: 122] |
| **Backend** | Python, Django, Django REST Framework (DRF)[cite: 122] |
| **AI / Computer Vision** | OpenCV, YOLOv8 (Ultralytics), FaceNet, Pandas, NumPy[cite: 60, 61, 123] |
| **Database & ORM** | MySQL, Django ORM[cite: 122] |
| **Development Tools** | Git, Local Development Server Environment[cite: 125] |

---

## 📊 System Design & Diagrams

The system architecture follows a clean client-server separation where the React frontend communicates asynchronously via JSON payloads with the secure Django REST backend[cite: 107].

* **Use Case Structure:** Distinct actor separation between regular *Employees*, *HR Admins*, and *Super Admins* controlling system permissions[cite: 111].
* **Data Flow Diagrams (DFDs):** Level 0 (Context) and Level 1/2 DFDs trace information from face image inputs and employee form submissions through database validation to final automated report generation[cite: 113, 116].

---

## 📂 Project Structure & Database Schema

The backend architecture organizes features across modular Django apps:
* `app/` — Core modules for documents, expenses, leave requests, payrolls, and travel[cite: 55, 56, 57, 58, 59]
* `attendance/` — Real-time face capture pipeline, logs, registers, and daily summaries[cite: 59, 60, 61]
* `auth/` — User accounts, groups, and role-based permissions[cite: 61, 62]
* `churn_prediction/` — Machine learning evaluation models and performance prediction logs[cite: 62, 63]
* `employee/` — Departments, designations, job types, and comprehensive employee records[cite: 63, 64, 65, 66]

---

## ⚙️ Installation & Setup

Follow these instructions to run the project locally for development or demonstration purposes.

### Prerequisites
* Python 3.10+
* Node.js & npm
* MySQL Server

### 1. Clone the Repository
```bash
git clone [https://github.com/mamun060/Python-Django-AI-Based-HRM.git](https://github.com/mamun060/Python-Django-AI-Based-HRM.git)
cd Python-Django-AI-Based-HRM

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install backend dependencies
pip install -r requirements.txt

# Configure your database settings in settings.py (MySQL credentials)
# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superadmin user
python manage.py createsuperuser

# Start the Django development server
python manage.py runserver

# Install frontend dependencies and start the app
npm install
npm run start
