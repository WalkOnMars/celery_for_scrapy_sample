from celery_app import app
from tutorial.spiders.quotes import QuotesSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def crawl_run():
    scope = 'all'
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(QuotesSpider, scope)
    process.start()
    process.join()

@app.task(queue='default')
def execute_task():
    return crawl_run()

