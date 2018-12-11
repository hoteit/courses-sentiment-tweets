# courses-sentiment-tweets
Coursera course reviews data set and sentiment analysis tweets using Google AutoML. 
This is setup for educational purposes as part of a lightning talk at the workplace

what is the idea?

Showcase how Google AutoML can be used in conjunction with Python libraries for accessing content from Twitter in order
to setup a sentiment analysis framework.

The requirements are as follows:
- Python virtual environment setup
- Docker container running PostGres database
- Python3 libraries for Google Cloud AutoML and Twitter access
- Google cloud storage and AutoML configuration 
- Jupyter notebook libraries for interactive transactions in Python
- Django to showcase a content management system for the project
- Twitter API access setup 


## Setup Django 

### Docker container setup

- install Docker and pull postgres image 
- create a postgres container off of the image
- in the configuration part, make sure to bind the volume so that the 
data does not get erased when the container is removed
- test that the database is connected


### Setup the code and Django 

- download the code from the github repository
- activate the virtual directory and install all the binary from requirements.txt
- migrate the Django model
- do a django runserver to make sure that everything is working fine


### Setup Twitter Development account
- access [developer.twitter.com](https://developer.twitter.com/content/developer-twitter/en.html)
- create a Twitter app at [https://developer.twitter.com/en/apps]
- get the permissions and add them under Django project settings in courses_sentiment_tweets/local_settings.py


### Setup Google Cloud AutoML 
###Training Model for the Course Reviews


The steps that you need to train Google AutoMl model for course reviews is as follows:

- setup a [google cloud](http://cloud.google.com) account 
- read the beginner's guide to using AutoMl for natural language at [https://cloud.google.com/natural-language/automl/docs/beginners-guide](https://cloud.google.com/natural-language/automl/docs/beginners-guide)
- download [Kaggle 100K Coursera's Course Reviews Dataset](https://www.kaggle.com/septa97/100k-courseras-course-reviews-dataset) or access the data set from folder with the same name inside the repo
- read the instructions on [preparing your training data](https://cloud.google.com/natural-language/automl/docs/prepare)
- setup a google cloud project for AutoML and a google cloud storage for the dataset. [quickstart](https://cloud.google.com/natural-language/automl/docs/quickstart) is useful here. 
- setup the dataset and manage the model. You can do this via the ui at [https://cloud.google.com/automl/ui/](https://cloud.google.com/automl/ui/) or through Python/Java/command line/nodejs as explained in [https://cloud.google.com/natural-language/automl/docs/models#automl-nl-example-web](https://cloud.google.com/natural-language/automl/docs/models#automl-nl-example-web)

My code is listed in coursera-reviews.ipynb as a Jupyter notebook
Note: that do use Google Cloud from your code, you need to setup GOOGLE_APPLICATION_CREDENTIALS using Google Cloud 
 Service Manager account. In my case it is  
    `export GOOGLE_APPLICATION_CREDENTIALS="/Users/tarek/.ssh/automlservice.txt"`
- check the results and validate your dataset through the AutoML UI listed. You can validate usihng the url listed above
or from your code 


