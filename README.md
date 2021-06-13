# school-simple-django-project
Prerequisites
1. Install Python
Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

2.Install Django
```bash
py -m pip install Django
```
3.Install MySQL
Install mysql-8.0.15. Follow the steps form the below reference document based on your Operating System. Reference: https://dev.mysql.com/doc/refman/5.5/en/

4.Install MySQL Client
```bash
pip install mysqlclient
```
Create Database in MySQL:
In your MySQL Command Line Client 
```bash
CREATE DATABASE sample; 
```
Clone git repository
https://github.com/vinaykabadagi/school.git

Edit project settings(settings.py)
```bash
# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'world',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}
```

Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver 
```
Try opening http://localhost:8000 in the browser. Now you are good to go.

Working:
<br>
