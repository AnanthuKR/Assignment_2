import sys
import time

from tweepy import StreamListener, OAuthHandler, Stream
import json
import argparse
from Conf import API_TOKEN, API_SECRET, ACCESS_SECRET, ACCESS_TOKEN, MONGO_DB, MONGO_PASSWORD
from MongoDB import PyMongoConnection
import datetime

data = []
pymongoCon = PyMongoConnection(MONGO_PASSWORD, MONGO_DB)


def process_data(raw_data):
    tweet_data = json.loads(raw_data)
    print(" .", end='')
    sys.stdout.flush()
    # print(tweet_data['user'])

    data.append({"t_id": tweet_data.get("id", "Null"),
                 "insertedAt": datetime.datetime.now(),
                 "createdAt": tweet_data.get('created_at', "NULL"),
                 "text": tweet_data.get("text", ""),
                 "likes": tweet_data.get("user", {}).get("favourites_count", "Null"),
                 "user_id": tweet_data.get("user", {}).get("id", "Null"),
                 "user_name": tweet_data.get("user", {}).get("screen_name", "Null"),
                 "profile_url": tweet_data.get("user", {}).get("profile_image_url", "Null")
                 }
                )

    if len(data) == 100:
        print("Completed")
        print("Inserting to MONGODB.............")
        pymongoCon.insert_data(data)
        print("Completed, Quitting program")
        exit(1)


class Listener(StreamListener):

    def on_data(self, raw_data):
        process_data(raw_data)

    def on_error(self, status_code):
        print(status_code)
        return False


class TwitterStream:

    def __init__(self, aut, listener):
        self.stream = Stream(auth=aut, listener=listener)
        self.batch = 0

    def start(self, tags=None):
        if tags is None:
            tags = []
        print("========================== Streaming Started ============================= \n")
        print("Streaming .")
        self.stream.filter(track=tags)


if __name__ == "__main__":

    listener = Listener()
    aut = OAuthHandler(API_TOKEN, API_SECRET)

    aut.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    stream = TwitterStream(aut, listener)
    stream.start(["python", "big data"])

