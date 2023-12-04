from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')
app = Celery('tasks')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings")
app.conf.broker_url = settings.CELERY_BROKER_URL


app.conf.beat_schedule = {
    'scraping-task-one-min': {
        'task': 'tasks.hackernews_rss',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks()




