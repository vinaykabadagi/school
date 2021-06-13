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
# Create Database in MySQL:
In your MySQL Command Line Client 
```bash
CREATE DATABASE sample; 
```
# Clone git repository
https://github.com/vinaykabadagi/school.git

# Edit project settings(settings.py)
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
# Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver 
```
Try opening http://localhost:8000 in the browser. Now you are good to go.

# Working:
If you are not logged in:
![Screenshot 2021-06-13 163811](https://user-images.githubusercontent.com/68753202/121805008-e1aeec80-cc66-11eb-9840-1ad6a33d33b1.png)

Log in page:
![Screenshot 2021-06-13 163844](https://user-images.githubusercontent.com/68753202/121805009-e2478300-cc66-11eb-98cf-0b6a08108665.png)

Home Page:
![Screenshot 2021-06-13 163900](https://user-images.githubusercontent.com/68753202/121805011-e2478300-cc66-11eb-917d-ce5a7ac593e1.png)

Adding a student:
![Screenshot 2021-06-13 163922](https://user-images.githubusercontent.com/68753202/121805012-e2e01980-cc66-11eb-9d29-eb9181bd7369.png)

Confirmation:
![Screenshot 2021-06-13 163934](https://user-images.githubusercontent.com/68753202/121805013-e378b000-cc66-11eb-93c5-eac7cef97c98.png)

Searching:
![Screenshot 2021-06-13 164026](https://user-images.githubusercontent.com/68753202/121805014-e378b000-cc66-11eb-8c1f-1881f75750b1.png)

Search Result:
![Screenshot 2021-06-13 164041](https://user-images.githubusercontent.com/68753202/121805016-e4114680-cc66-11eb-92a3-3fd844647066.png)

Updating:
![Screenshot 2021-06-13 164108](https://user-images.githubusercontent.com/68753202/121805017-e4114680-cc66-11eb-8dff-8873e1d57195.png)

After Update:
![Screenshot 2021-06-13 164141](https://user-images.githubusercontent.com/68753202/121805019-e4a9dd00-cc66-11eb-8090-383a50d9830e.png)

Delete Student:
![Screenshot 2021-06-13 164203](https://user-images.githubusercontent.com/68753202/121805020-e5427380-cc66-11eb-992a-a509af214c9c.png)

After deletion:
![Screenshot 2021-06-13 164221](https://user-images.githubusercontent.com/68753202/121805007-e07dbf80-cc66-11eb-9893-f01936302efa.png)
