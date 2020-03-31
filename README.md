# Autama Backend
* API
* DB
* Supporting infrastructure

# To Run:
  * pip install -r requirements.txt
  * python manage.py runserver
  * in a web browser go to: 127.0.0.1:8000 (This should be displayed during server startup)

# To Recreate the DB
* Python manage.py makemigrations accounts
* Python manage.py makemigrations AutamaProfiles
* Python manage.py migrate
