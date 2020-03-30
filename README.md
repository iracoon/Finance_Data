# finance_data

PROJECT SET UP GUIDE

1)	Make sure Python 3, not Python 2, is the default on your machine (python --version)
  https://www.python.org/downloads/ (install if you don’t already have it)

2)	Download MySQL 

  a) Install MySQL (with workbench) on your machine
https://www.youtube.com/watch?v=u96rVINbAUI

  b) (run this command in workbench using your own credentials)
ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';

  c) create a database named “finance_data”

3)	I am using “Sublime” as my IDE but you can use whatever you want
  https://www.sublimetext.com/3
  
4)	Clone Repo
  git clone https://github.com/iracoon/finance_data.git
  
5)	Create an “.env” file under the “finance_data/finance_data.” (Should be in the same folder as settings.py)

  contents of “.env” should look like this (except with your database credentials):

  USER=root
  PASSWORD=password
  PORT=3306

6)	Download necessary python packages listed below (if not already installed on your machine)
  pip install django
  pip install django-environ
  pip install django-crispy-forms
  pip install pandas
  pip install mysqlclient (you need to have Visual C++ Build Tools installed for this to work, if you run into errors I recommend this https://stackoverflow.com/questions/26866147/mysql-python-install-error-cannot-open-include-file-config-win-h)

7)	(cd into finance_data folder (where manage.py is located) and run these commands)
  python manage.py migrate (this should create a bunch of empty tables in your finance_data db)
  python manage.py createsuperuser (this gives you admin privileges)
  python manage.py create_data PFDcomp.txt analysis_compensation (this should create/populate a new table in your db called “analysis_compensation”)

8)	run development server

  python manage.py runserver

9)	Make sure everything is working as it should

  http://127.0.0.1:8000/search/ (should be fetching data from the “analysis_compensation” table)

  http://127.0.0.1:8000/admin (should be able to login to this using your super user created before)
