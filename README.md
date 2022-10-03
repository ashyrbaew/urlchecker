# urlchecker

### Simple app to periodically check url HTTP responses


## Technical requirements for Project:
    Python >= 3.8
    Django >= 32
    Redis = 4.3.4
    Celery = 5.2.7

    * For details, please refer to requirements.txt
---

## Project Description
This app checks links added by registered users and shows response in highlighted with color,  if the response not 200 in red color
otherwise in green, You can also manage urls via admin panels or by logging in to system

Implemented also API at /urls/api path, you can customize this project to use
as API designed app 
inorder to test please follow below steps 

---


## Running Project locally
* Below commands copies the project to your machine and runs locally
simply follow steps

```bash
$ git clone https://github.com/ashyrbaew/urlchecker.git
$ virtualenv -p python3.9 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
* copy/rename and update .env_sample file as .env, with same folder as settings.py,
by default it is set up for Production environment
* update .env file settings(db, etc) according to your system
* Run next command:
```bash
$ python manage.py migrate
$ python ./manage.py runserver
```

---

## Starting Project at Production server, follow below steps:
* copy/rename and update .env_sample file located at project root dir as .env, with same folder as settings.py,
by default it is set up for Production environment
* Run below commands, by default it automatocally craetes admin user with admin password
<b>update admin password immediately since its done for test purposes only</b>

```bash
$ git clone https://github.com/ashyrbaew/urlchecker.git
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

