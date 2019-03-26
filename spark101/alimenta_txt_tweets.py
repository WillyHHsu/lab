from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credentials
import json
import time

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
        
    def __init__(self, fetched_tweets_filename, time_limit=1):        
        
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        self.fetched_tweets_filename = fetched_tweets_filename
        self.start_time = time.time()
        self.limit = time_limit

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit:
            try:
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write({'id':json.loads(data)['id']
                         ,'text':json.loads(data)['text']})
                return True
            except BaseException as e:
                print("Error on_data {}".format(e))
                return True
        else:
            return False
            
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
 
    hash_tag_list = ["bolsonaro"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
