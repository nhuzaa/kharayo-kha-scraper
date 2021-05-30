#!/bin/bash

cd /app/scraper
uvicorn wakeup:app --host 0.0.0.0 --port 8000 &&
while true; do
  scrapy crawl onlinekhabar && scrapy crawl ekantipur
  sleep 1200 
done
