from celery import Celery
from celery_beat import task_schedule

app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379/0')
app.conf.beat_schedule = task_schedule
