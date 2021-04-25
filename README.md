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

### 3.6 Creating Custom User Admin

        modified:   app/users/__pycache__/admin.cpython-39.pyc
        new file:   app/users/__pycache__/forms.cpython-39.pyc
        modified:   app/users/admin.py
        modified:   app/users/forms.py
        modified:   db.sqlite3

### 3.7 Testing

        modified:   README.md
        new file:   app/users/__pycache__/tests.cpython-39.pyc
        modified:   app/users/tests.py

        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> python manage.py test app.users.tests
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        ..

        ---

        Ran 2 tests in 0.279s

        OK
        Destroying test database for alias 'default'...

## CHAPTER 4: Pages App

### 4.1 Create 'pages' app

    (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> mkdir app\pages

    (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> python manage.py startapp pagrs.testses app\pages

        modified:   README.md
        new file:   app/pages/__init__.py
        new file:   app/pages/admin.py
        new file:   app/pages/apps.py                                                         ustom User Admin"
        new file:   app/pages/migrations/__init__.py
        new file:   app/pages/models.py
        new file:   app/pages/tests.py
        new file:   app/pages/views.py

### 4.2 Register pages app to project root

        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> tree app /f
        Folder PATH listing
        Volume serial number is DC72-8D6C
        E:\2021\DJANGO\PROJECTSEXEBOOKS\BOOKSTORE10K\SRC\APP
        ├───pages
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │   │   __init__.py
        │   │   │
        │   │   └───__pycache__
        │   │           __init__.cpython-39.pyc
        │   │
        │   └───__pycache__
        │           admin.cpython-39.pyc
        │           apps.cpython-39.pyc
        │           models.cpython-39.pyc
        │           __init__.cpython-39.pyc
        │
        └───users
        modified:   README.md
        new file:   app/pages/__pycache__/__init__.cpython-39.pyc
        new file:   app/pages/__pycache__/admin.cpython-39.pyc
        new file:   app/pages/__pycache__/apps.cpython-39.pyc
        new file:   app/pages/__pycache__/models.cpython-39.pyc
        modified:   app/pages/apps.py
        new file:   app/pages/migrations/__pycache__/__init__.cpython-39.pyc
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py

### 4.3 Template, URLs and Views

