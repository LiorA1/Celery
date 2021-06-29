from __future__ import absolute_import, unicode_literals

# https://stackoverflow.com/questions/50671044/apps-arent-loaded-yet-when-trying-to-import-model-in-a-celery-tasks-file

# https://stackoverflow.com/questions/50336688/django-load-production-settings-for-celery

import os

from celery import Celery

# Define Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project', broker='amqp://', backend='rpc://')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# https://www.youtube.com/watch?v=kWxYPq7Sc8A&list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20&index=6&t=1s