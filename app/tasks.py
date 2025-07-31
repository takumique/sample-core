import os

from celery import Celery

from reporter import Reporter


REPORTER_ADDR = os.environ['REPORTER_ADDR']
REPORTER_PORT = int(os.environ['REPORTER_PORT'])

reporter = Reporter(REPORTER_ADDR, REPORTER_PORT)
reporter.publish_core_server_state("UP")

REDIS_DNS_NAME = os.environ['REDIS_DNS_NAME']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_DATABASE = os.environ['REDIS_DATABASE']
REDIS_URL = f"redis://{REDIS_DNS_NAME}:{REDIS_PORT}/{REDIS_DATABASE}"

CORE_NAME = "core"

core_app = Celery(
    CORE_NAME,
    broker=REDIS_URL,
    backend=REDIS_URL,
)
core_app.conf.update(
    result_timeout=30,
)

# tasks

@core_app.task()
def hello(message):
    task_id = hello.request.id
    return "world!"

# main

if __name__ == '__main__':
    core_app.start()
