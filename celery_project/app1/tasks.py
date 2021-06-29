from __future__ import absolute_import, unicode_literals

#from celery import shared_task
from celery_project.celery import app
from celery.decorators import task


#@shared_task
@app.task(name='add')
def add(x, y):
    return x + y

#@shared_task
@app.task
def reverse(name):
    return name[::-1]