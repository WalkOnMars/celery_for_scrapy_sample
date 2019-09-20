# celery_for_scrapy_sample


my environment: celery 3.1.25/ python 3.69/ redis 2.10.6/ windows10

## 1. in celery_config.py file, change crontab to change trigger time, my scrapy will start crawl at 18:29:00 for below setting
```
CELERYBEAT_SCHEDULE = {
    'multiply-at-some-time': {
        'task': 'tasks.execute_task',
        'schedule': crontab(hour=18, minute=29),   # 每天早上 6 点 00 分执行一次
        'args': ()                                  # 任务函数参数
    }
}
```
## 2. execute command like this in terminal 1:
```
celery -A celery_app worker -Q default --loglevel=info
```
## 3. execeute command like this in terminal 2:
```
celery -A celery_app beat 
```
## 4. part result:
```
[2019-09-20 18:29:04,015: WARNING/Worker-1] 2019-09-20 18:29:04 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 2642,
 'downloader/request_count': 10,
 'downloader/request_method_count/GET': 10,
 'downloader/response_bytes': 24444,
 'downloader/response_count': 10,
 'downloader/response_status_count/200': 10,
 'dupefilter/filtered': 1,
 'elapsed_time_seconds': 3.696511,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2019, 9, 20, 10, 29, 4, 13369),
 'item_scraped_count': 100,
 'log_count/DEBUG': 111,
 'log_count/INFO': 10,
 'log_count/WARNING': 121,
 'request_depth_max': 10,
 'response_received_count': 10,
 'scheduler/dequeued': 10,
 'scheduler/dequeued/memory': 10,
 'scheduler/enqueued': 10,
 'scheduler/enqueued/memory': 10,
 'start_time': datetime.datetime(2019, 9, 20, 10, 29, 0, 316858)}
[2019-09-20 18:29:04,026: INFO/Worker-1] Spider closed (finished)
[2019-09-20 18:29:04,026: WARNING/Worker-1] 2019-09-20 18:29:04 [scrapy.core.engine] INFO: Spider closed (finished)
[2019-09-20 18:29:04,032: INFO/MainProcess] Task tasks.execute_task[cf74027b-d03b-4f75-87fa-14bcc585955b] succeeded in 4.016000000061467s: None

```

