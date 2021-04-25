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

        modified:   README.md
        new file:   app/pages/__pycache__/urls.cpython-39.pyc
        new file:   app/pages/__pycache__/views.cpython-39.pyc
        new file:   app/pages/urls.py
        modified:   app/pages/views.py
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/__pycache__/urls.cpython-39.pyc
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/_base.html
        new file:   templates/home.html

### 4.4 Testing

        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> python manage.py test app.pages.tests
        System check identified no issues (0 silenced).
        ..
        ----------------------------------------------------------------------
        Ran 4 tests in 0.028s

        modified:   README.md
        modified:   app/pages/__pycache__/tests.cpython-39.pyc
        modified:   app/pages/tests.py

### 4.5 Final test

        (venv39227) PS E:\2021\DJANGO\ProjectsExEbooks\BookStore10k\src> python manage.py test app.pages.tests
        System check identified no issues (0 silenced).
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.056s

        modified:   README.md
        modified:   app/pages/__pycache__/tests.cpython-39.pyc
        modified:   app/pages/tests.py

## CHAPTER 5: User Registration

### 5.1 Checking the auth app is installed

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py

### 5.2 Auth URLs and Views        

        http://127.0.0.1:8000/accounts/registrazione/

        Page not found (404)
        Request Method: GET
        Request URL:    http://127.0.0.1:8000/accounts/

        accounts/ login/ [name='login']
        accounts/ logout/ [name='logout']
        accounts/ password_change/ [name='password_change']
        accounts/ password_change/done/ [name='password_change_done']
        accounts/ password_reset/ [name='password_reset']
        accounts/ password_reset/done/ [name='password_reset_done']
        accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
        accounts/ reset/done/ [name='password_reset_complete']

        modified:   README.md
        modified:   config/__pycache__/urls.cpython-39.pyc
        modified:   config/urls.py

### 5.3 Modify the Homepage to check if a user is already logged in or not     

        # reference
        https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.views

        # the result
        http://127.0.0.1:8000/
        
        Homepage
        Hi admin@admin.com!

### 5.4 Django Source Code        

        https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/contrib/auth/urls.py

        # django/contrib/auth/urls.py
        from django.contrib.auth import views
        from django.urls import path

        urlpatterns = [
            path('login/', views.LoginView.as_view(), name='login'),
            path('logout/', views.LogoutView.as_view(), name='logout'),

            path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
            path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
            
            path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
            path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
            path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
            path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
        ]        

### 5.5 Login

        # After logged in and then logged out from the admin panel, then when clicked the login url, it displayed error:   
        TemplateDoesNotExist at /accounts/login/
        registration/login.html      

        # How to solve it?
        > create login page at: registration/login.html 

        # add login form template

        modified:   README.md
        modified:   db.sqlite3
        new file:   templates/registration/login.html