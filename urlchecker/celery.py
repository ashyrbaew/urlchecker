import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlchecker.settings')
app = Celery('urlchecker')

app.conf.beat_schedule = {
    "update_every_5_min": {
        "task": 'main.views.update_url_statuses_db',
        "schedule": crontab(minute='*/2'),
        "args": ['5']
    },
    "update_every_10_min": {
        "task": 'main.views.update_url_statuses_db',
        "schedule": crontab(minute='*/3'),
        'args': ['10']
    },
    "update_every_15_min": {
        "task": 'main.views.update_url_statuses_db',
        "schedule": crontab(minute='*/5'),
        'args': ['15']
    }
}

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
