## Django-Students-Ecommerce-💯💯
### Online Ecommerce store for tertiary students living in residence.

### Website link: **https://www.resgetit.com/

### Project Description
- I developed this project as student studying at University Of Johannersburg for students in my residence to eliminate their challenges in order for them  to be able to have access to essential products which are not provided near by, the  website will allow them to order some products or services and be delivered to them within 10 minutes in which it will eliminate the challenge to go miles to buy general product such as snacks and it will play positive role in decreasing covid19 cases since it will be helping about 1500+ students
-frontend tools: html css bootstrap4 and jquery
-Project backend code can be used for any sort of production
-Project frontend code can not be used in any sort of production since the code is licensed and working in existing production 


### eCommerce Project Features Listing
- Admin adds the category and products
- Admin can upload advertising or sales on the Months_Specials model which triggers a modal popup when a user visits the website
- Browses all the products and categories
- User can can order and checkout without signing in
- User can can order services provided in web
- User can browse special in the store
- Search all the products using filters
- Add products in cart
- User can checkout product

### To clone the project on Linux(use Git Bash Software on Windows):
1.First Create a Virtual Environment `python -m venv venv`<br/><br/>
2.Then type `cd venv` To Move To Virtual Environment directory<br/><br/>
3.Clone This Project git clone `https://github.com/sajib1066/django-ecommerce.git`<br/><br/>
4.Activate Virtual Environment: `source bin/activate` or on Windows `source scripts/activate`<br/><br/>
5.Install Requirements Package: `pip install -r requirements.txt`<br/><br/>
6.Make Migrations for all apps: `python manage.py makemigrations GetItApp` ..NOTE:there are two more apps you must make migrations for namely cart and orders<br/><br/>
7.Migrate Database: `python manage.py migrate`<br/><br/>
8.Create Super User `python manage.py createsuperuser`<br/><br/>
9.Finally Run The Project python `manage.py runserver`<br/><br/>
