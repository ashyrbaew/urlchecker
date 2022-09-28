# urlchecker

### Simple app to check url statuses


## Technical requirements for Project:
    Python >=3.8
    Django 2.2
---

## Project Description
A simple app which can import huge CSV files into DB using Python/Django
and provide it via API. To test it, please follow below steps:

---


## Running Project locally
* Below commands copies the project to your machine and runs locally 

```bash
$ git clone https://github.com/ashyrbaew/csv_to_db.git
$ virtualenv -p python3.9 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
* copy/rename and update .env_sample file into project root dir as .env, with same folder as settings.py,
by default it is set up for Production environment
* update .env file settings(db, etc) according to your system
* Run below 2 commands at project directory, first command is to import
large csv files into db, just `python manage.py import_csv path/to/file.csv`
```bash
$ python manage.py import_csv /Users/akylbek/Desktop/test_data.csv
$ python ./manage.py runserver
```

---

## Starting Project at Production server, follow below steps:
* copy/rename and update .env_sample file into project root dir as .env, with same folder as settings.py,
by default it is set up for Production environment
* It will automatically imports test_data.csv file into postgres db 
* Automaticllay creates user admin, with password admin, so, you can open
djangos built-in admin panel and login with above user/pass to check 

```bash
$ git clone https://github.com/ashyrbaew/csv_to_db.git
$docker-compose build .
$docker-compose up
```

---

## Architecture

**admin** - contains admin panel settings and configurations,

**Views** - contains logic for accepting request data and passing to Forms and Services

**Urls** - contains URL matching patterns with Views

**Models** - contains data and object presentation logic

**Settings** - Contains Project common settings like DB, Time, etc

**Api** - contains only API presentation app implemented with FastAPI framework


## nginx

Nginx is used as a reverse proxy server, thus, all web traffic goes though it and Django is not in public network.
See more details at nginx configs at nginx/conf.d/sites-available

