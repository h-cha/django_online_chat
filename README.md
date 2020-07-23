# django_online_chat

# Requirement

* Python 3.7.7
* Django 2.0.5
* channels 2.1.1
* channels_redis
* docker 18.03.0-ce
 
# Installation

```bash
$ pip install --upgrade pip
$ pip install django channels
$ python3 -m pip install channels_redis
```
 
# Usage


```bash
$ git clone https://github.com/h-cha/django_online_chat
$ cd django_online_chat
$ python manage.py migrate
$ python manage.py runserver

```

* DOCKER
```bash
$ docker run -p 6379:6379 -d redis:5
```

* access
http://localhost:8000/accounts

 
