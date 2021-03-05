## Django-Students-Ecommerce-
# Online Ecommerce store for tertiary students living in residence.

# Website link: **https://www.resgetit.com/

# To clone the project on Linux(use Git Bash Software on Windows):
1.First Create a Virtual Environment `python -m venv venv`
2.Then type `cd venv` To Move To Virtual Environment directory
3.Clone This Project git clone `https://github.com/sajib1066/django-ecommerce.git`
4.Activate Virtual Environment: `source bin/activate` or on Windows `source scripts/activate`
5.Install Requirements Package: `pip install -r requirements.txt`
6.Make Migrations for all apps: `python manage.py makemigrations GetItApp` ..NOTE:there are two more apps you must make migrations for namely cart and orders
7.Migrate Database: `python manage.py migrate` 
8.Create Super User `python manage.py createsuperuser`
9.Finally Run The Project python `manage.py runserver`
