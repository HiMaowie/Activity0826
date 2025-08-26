# Activity0826 — Django Tweet & History App

This project demonstrates the use of **Django Signals** and the **built-in User model**. It allows users to create tweets and automatically logs each tweet creation in a separate History app.

## Features
- User authentication (login/logout via Django's built-in auth system)
- Create and post tweets
- Automatically logs tweet creation using Django signals
- Homepage with a link to create tweets
- Admin panel to manage tweets and history records

---

## Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

---

## 1. Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/HiMaowie/Activity0826.git
cd Activity0826
```

2. Create a Virtual Environment
python -m venv venv


Activate the virtual environment:

Windows (CMD):

venv\Scripts\activate


Windows (PowerShell):

venv\Scripts\Activate.ps1


macOS/Linux:

source venv/bin/activate

3. Install Dependencies

If a requirements.txt file is provided, run:

pip install -r requirements.txt


If not, install Django manually:

pip install django

4. Apply Migrations

Run the following to set up your database schema:

python manage.py migrate

5. Create a Superuser (for admin access)
python manage.py createsuperuser


Follow the prompts to set up a username and password.

6. Run the Development Server
python manage.py runserver


Visit the following in your browser:

Homepage: http://127.0.0.1:8000/

Tweet creation: http://127.0.0.1:8000/tweet/create/

Admin panel: http://127.0.0.1:8000/admin/

7. File & Directory Notes

Tweets are created via /tweet/create/ and logged in the History app.

A signal in tweet/signals.py automatically creates a history entry after each tweet.

.gitignore excludes:

Virtual environment folder (venv/)

Database file (db.sqlite3)

Cache files (__pycache__/)

8. Stopping the Server

Press CTRL + C in the terminal where the server is running.

9. Additional Notes

If you add more packages, run:

pip freeze > requirements.txt


to update your dependency list.

Make sure to activate your virtual environment every time you work on the project.
