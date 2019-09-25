# excel-2019-django-cms
# Excel Mec REST api
## Steps for setting up the backend REST api

1) Install mysql server
```
sudo apt-get install mysql-server
```
2) Create a user on mysql.
[How to create a new user on mysql and grant access.](https://www.a2hosting.in/kb/developer-corner/mysql/managing-mysql-databases-and-users-from-the-command-line)

3) Install linux dependencies.
```
sudo apt-get install python-mysqldb libmysqlclient-dev python-dev
```
4) Go the to the directory excel_2019_django_cms/excel_2019_django_cms and duplicate the file secret.py.example with the name secret.py and give configurations there.
4) Create and activate a virtual environment
```
virtualenv -p python3 env
source env/bin/activate
```
5) Install python dependencies
```
pip install -r requirements.txt
```
6) Make migrations
```
python manage.py makemigrations
python manage.py migrate
```
7) Run the server
```
python manage.py runserver
```
## Docs
[https://docs.djangoproject.com/en/2.2/](https://docs.djangoproject.com/en/2.2/)
[https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
[https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html](https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html)
