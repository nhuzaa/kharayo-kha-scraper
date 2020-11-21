#!/bin/bash

# uvicorn wakeup:app --host 0.0.0.0 --port 5000 &&
while true; do
  cd /app/scraper
  scrapy crawl onlinekhabar && scrapy crawl ekantipur
  sleep 1200 
done
