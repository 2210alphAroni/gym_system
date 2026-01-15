A role-based Gym Management & Workout Assignment System built using Django & Django REST Framework.
This project provides a secure REST API to manage gym branches, users, workout plans, and workout tasks with strict business rules.

⚠️ This is a backend-only project. No frontend is included.

📖 Project Background

A fitness company needs an internal system to manage:

Multiple gym branches

Trainers & members

Workout plans

Workout tasks assigned to members

Different users have different responsibilities, and data isolation between gym branches is mandatory.

🚀 Tech Stack

Backend: Django, Django REST Framework

Authentication: JWT (SimpleJWT)

Database: SQLite (Development)

API Testing: Postman

Deployment: Hosted API (Public URL)

👥 User Roles & Permissions
🔑 Super Admin

Create & manage gym branches

Create Gym Managers

View all data across all branches

Bypass branch restrictions

🏢 Gym Manager

Manages one gym branch

Create Trainers (max 3 per branch)

Create Members

View all users & workouts in their branch

🏋️ Trainer

Belongs to one gym branch

Create workout plans

Assign workout tasks to members of their own branch only

Update workout task status

👤 Member

Belongs to one gym branch

View only their assigned workout tasks

Update their own task status (pending → completed)

🔐 Authentication & Authorization

JWT-based authentication (access + refresh)

All APIs are protected except login

Role-based permission system

Users cannot access data from another branch

🧱 Core Models (Entities)
User

Email (unique)

Password (hashed)

Role (Admin / Manager / Trainer / Member)

Gym Branch (nullable for Super Admin)

Created at

GymBranch

Name

Location

Created at

WorkoutPlan

Title

Description

Created by (Trainer)

Gym branch

Created at

WorkoutTask

Workout plan

Member

Status (pending, in_progress, completed)

Due date

Created at

🧠 Business Rules (Strictly Enforced)

Trainer cannot assign tasks to members of another branch

Member cannot update another member’s task

Manager cannot create users outside their branch

A branch can have maximum 3 trainers

Member cannot view workout plans directly

Super Admin can bypass branch restrictions

📡 API Features
🔑 Authentication

Login

Refresh token

Get current user profile

🏢 Gym Branch Management

Super Admin can create & list branches

👥 User Management

Manager creates Trainers & Members (branch-specific)

Manager lists users of their branch

🏋️ Workout Plan Management

Trainer creates workout plans

Manager views all workout plans in their branch

📋 Workout Task Management

Trainer assigns workout tasks

Trainer updates task status

Member views & updates their own tasks

⚙️ Project Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/2210alphAroni/gym_system
cd gym-management-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Create Super Admin
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver

