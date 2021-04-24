# BUILDING A BOOKSTRORE APP USING DJANGO 2.2.7

## CHAPTER 1: SETUP

### 1.1 Create virtual environment

## CHAPTER 2: Using Default Database

        > Default db (sqlite3) will be use
        > PASS

## CHAPTER 3: Bookstore Project

### 3.1 Create django project src/config

        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src>django-admin startproject config .
        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> tree /f
        Folder PATH listing
        Volume serial number is DC72-8D6C
        E:.
        │   .gitignore
        │   manage.py
        │   README.md
        │
        └───config
                settings.py
                urls.py
                wsgi.py
                __init__.py

### 3.2 Creating users app for Custom User Model

    (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> mkdir app\users

    (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> python manage.py startapp users  app\users

    (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> tree app /f
    Folder PATH listing
    Volume serial number is DC72-8D6C
    E:\2021\DJANGO\PROJECTSEXEBOOKS\BOOKSTORE10K\SRC\APP
    └───users
        │   admin.py
        │   apps.py
        │   models.py
        │   tests.py
        │   views.py
        │   __init__.py
        │
        └───migrations
                __init__.py

### 3.3 Install users app to root dir

        modified:   README.md
        new file:   app/users/__pycache__/__init__.cpython-39.pyc
        new file:   app/users/__pycache__/admin.cpython-39.pyc
        new file:   app/users/__pycache__/apps.cpython-39.pyc
        new file:   app/users/__pycache__/models.cpython-39.pyc
        modified:   app/users/apps.py
        new file:   app/users/migrations/__pycache__/__init__.cpython-39.pyc
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py

### 3.4 Creating CustomUser model

        modified:   README.md
        modified:   app/users/__pycache__/models.cpython-39.pyc
        new file:   app/users/migrations/0001_initial.py
        new file:   app/users/migrations/__pycache__/0001_initial.cpython-39.pyc
        modified:   app/users/models.py
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py
        modified:   db.sqlite3

### 3.5 Creating User Forms

        modified:   README.md
        new file:   app/users/forms.py
