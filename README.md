# django_online_chat

# Requirement

Python 3.7.7
Django 2.0.5
channels 2.1.1
channels_redis
docker
 
# Installation
 
$ pip install --upgrade pip
$ pip install django channels
$ python3 -m pip install channels_redis
 
# Usage

'''docker
docker run -p 6379:6379 -d redis:5
'''

```bash
git clone https://github.com/h-cha/django_online_chat
cd django_channels
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
 
