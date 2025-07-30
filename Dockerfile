FROM python:3.13.2-slim

RUN mkdir -p /usr/bin/sample
COPY ./requirements.txt /usr/bin/sample
COPY ./app /usr/bin/sample

RUN mkdir -p /usr/bin
COPY ./run-sample-core.sh /usr/bin
RUN chmod 0755 /usr/bin/run-sample-core.sh

WORKDIR /usr/bin/sample
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["celery", "-A", "tasks", "worker", "--loglevel", "info", "--pool", "solo", "--concurrency", "1"]
