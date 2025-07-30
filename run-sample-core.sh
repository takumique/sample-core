#!/bin/sh

cd /usr/bin/sample

celery -A tasks worker --loglevel info --pool solo --concurrency 1
