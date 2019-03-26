from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json
import time
import os

class TwitterStreamer():

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)
        
class StdOutListener(StreamListener):
        
    def __init__(self, fetched_tweets_filename, time_limit=30):        
        
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        self.fetched_tweets_filename = fetched_tweets_filename
        self.start_time = time.time()
        self.limit = time_limit

    def on_data(self, data):
        try:
            if (time.time() - self.start_time) < self.limit:

                    a = {'id':json.loads(data)['id']
                         ,'text':json.loads(data)['text']}
        
                    with open(self.fetched_tweets_filename, 'a') as tf:

                       tf.write(json.dumps(a)+'\n')
                    
                    return True
            else:
                return False
        except Exception as err:
            print(err)
            return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':

    while 1 == 1:
        
        hash_tag_list = ["bolsonaro"]
        fetched_tweets_filename = "tweets.txt"
        twitter_streamer = TwitterStreamer()
        twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
        try:
            for i in open("tweets.txt", "r").read().split('\n'):
                with open('tweets/{}.json'.format(json.loads(i)['id']), 'w') as tf:
                    json.dump(json.loads(i), tf)
        except:
            pass
        os.remove("tweets.txt")
