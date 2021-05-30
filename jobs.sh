#!/bin/bash

cd /app/scraper
uvicorn wakeup:app --host 0.0.0.0 --port 8000 &&

 scrapy list|xargs -n 1 scrapy crawl

