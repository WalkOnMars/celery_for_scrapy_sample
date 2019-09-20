#-*-coding=utf-8-*-
from __future__ import absolute_import

from celery.schedules import crontab
# 中间件
BROKER_URL = 'redis://localhost:6379/6'
# 结果存储
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/5"
# 默认worker队列
CELERY_DEFAULT_QUEUE = 'default'
# 异步任务
CELERY_IMPORTS = (
    "tasks"
)

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = False

from datetime import timedelta
# celery beat
CELERYBEAT_SCHEDULE = {
    'multiply-at-some-time': {
        'task': 'tasks.execute_task',
        'schedule': crontab(hour=18, minute=29),   # 每天早上 6 点 00 分执行一次
        'args': ()                                  # 任务函数参数
    }
}
