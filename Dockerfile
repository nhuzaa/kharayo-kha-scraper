# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3
 
# Set the working directory to /app.
RUN mkdir /config
WORKDIR /config
 
# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
COPY .env ./
COPY ./firebase.json ./firebase.json
 
# Install Scrapy specified in requirements.txt.
RUN pip3 install --upgrade pip 
RUN pip3 install --no-cache-dir -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY ./app/scraper /app/
 
# Run the crawler when the container launches.
# CMD [ "python3", "./go-spider.py" ]
CMD echo kharayo ayoo...!!
