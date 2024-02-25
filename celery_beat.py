from celery.schedules import crontab

task_schedule = {
    'your_task': {
        'task': 'tasks.your_task_method_name',
        'schedule': crontab(minute='*/1')
    }
}