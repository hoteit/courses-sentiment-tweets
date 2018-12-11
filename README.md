# courses-sentiment-tweets
Coursera course reviews data set and sentiment analysis tweets using Google AutoML. This is setup for educational purposes as part of a lightning talk at the workplace

what is the idea?

Showcase how Google AutoML can be used in conjunction with Python libraries for accessing content from Twitter in order
to setup a sentiment analysis framework.

The requirements are as follows:
- Python virtual environment setup
- Docker container running PostGres database
- Python3 libraries for Google Cloud AutoML and Twitter access
- Google cloud storage and AutoML confiruation 
- Jupyter notebook libraries for interactive transactions in Python
- Django to showcase a content management system for the project
- Twitter API access setup 


## Setup

### Docker container setup

- install Docker and pull postgres image 
- create a postgres container off of the image
- in the configuration part, make sure to bind the volume so that the 
data does not get erased when the container is removed
- test that the database is connected