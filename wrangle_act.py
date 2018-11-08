# The dataset that will be wrangled (and analyzd and visualizd)
# is the tweet archive of Twitter user @dog_rates, also known as
# WeRateDogs. WeRateDogs is a Twitter account that rates people's
# dogs with a humorous comment about the dog.

import pandas as pd
import numpy as np
import requests
import os
import tweepy
import simplejson as json

# Data Gathering
# Task 1:  load data from WeRateDogs Twitter archive
# in `twitter-archive-enhanced.csv`
archive_df = pd.read_csv('twitter-archive-enhanced.csv')

# Task 2: download online data (tweet image predictions)
# using Requests library from URL
url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
r = requests.get(url)

with open('image_predictions.tsv', mode='wb') as f:
    f.write(r.content)

image_df = pd.read_csv('image_predictions.tsv', sep='\t')

# Task 3: query the Twitter API for each tweet's JSON data
# using Python's Tweepy library and store each tweet's entire
# set of JSON data in a file called `tweet_json.txt`.

# create an API object
consumer_key = 'my_consumer_key'
consumer_secret = 'my_consumer_secret'
access_token = 'my_access_token'
access_secret = 'my_access_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweet_id_list = archive_df['tweet_id']

# Using time module to record the query process
import time
start = time.time()
# query API for info
i = 0
j = 0
for tweet_id in tweet_id_list:
    try:
        status = api.get_status(tweet_id, tweet_mode='extended')
        data = status._json
        with open('tweet_json.txt', 'a') as file:
            json.dump(data, file)
            file.write('\n')
        print('Tweet ID {} data found!'.format(tweet_id))
        i += 1
    except:
        print('Tweet ID {} data not found!!!'.format(tweet_id))
        j += 1
end = time.time()
print(end-start)

# Read the file `tweet_json.txt` and extract information of interest
df_list = []
with open('tweet_json.txt') as file:
    for line in file:
        data = json.loads(line)
        tweet_id = str(data['id'])
        retweet_count = data['retweet_count']
        favorite_count = data['favorite_count']
        text = data['full_text']
        df_list.append({'tweet_id': tweet_id, 'retweet_count': retweet_count,
                            'favorite_count': favorite_count, 'text': text})

tweet_json_df = pd.DataFrame(df_list, columns = ['tweet_id', 'retweet_count', 'favorite_count', 'text'])
