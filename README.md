Install python if not available

`https://www.python.org/downloads/macos/`

create Virtual environment 

`python3 -m venv ./devenv`

Activate Virtual Environment

`source devenv/bin/activate`

Install the existing requirements to run this project
`pip install -r requirements.txt`

to freeze the append the newly added libraries to requirements.txt
`pip freeze > requirements.txt`


Install all the Django libraries

 `pip install django, django-rest-framework`
 `pip install djangorestframework-simplejwt`

 start a new project in django

 `python -m django startproject backend`

navigate to backend folder
`python manage.py startapp myApi`

Add the way of authentication via REST_FRAMEWORK (via web browser)

add simplejwt configurations in settings.py which is provided in official django documentation

Allow all calls from other apps in settings.py
`CORS_ALLOW_ALL_ORIGINS = True`

Make migartions when you change anything in models
`python manage.py makemigrations`
`python manage.py migrate`

To run the application
`python manage.py runserver`

