from __future__ import absolute_import
from celery import Celery

app = Celery('celery_app')
app.config_from_object('celery_config')
