#!/bin/bash

while true; do
  cd /app/scraper
  scrapy crawl onlinekhabar && scrapy crawl ekantipur
  sleep 1200 
done
