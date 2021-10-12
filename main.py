from tweepy import StreamListener, OAuthHandler, Stream
import json
import argparse
from Conf import API_TOKEN, API_SECRET, ACCESS_SECRET, ACCESS_TOKEN, MONGO_DB, MONGO_PASSWORD
from MongoDB import PyMongoConnection

data = []
pymongoCon = PyMongoConnection(MONGO_PASSWORD, MONGO_DB)


def process_data(raw_data):
    tweet_data = json.loads(raw_data)
    print(tweet_data.get("user").get("favourites_count"))

    data.append({"t_id": tweet_data.get("id", "Null"),
                 "createdAt": tweet_data.get('created_at', "NULL"),
                 "text": tweet_data.get("text", ""),
                 "likes": tweet_data.get("user", {}).get("favourites_count", "Null"),
                 "user_id": tweet_data.get("user", {}).get("id", "Null"),
                 "user_name": tweet_data.get("user", {}).get("screen_name", "Null"),
                 }
                )
    if len(data) == 10:
        pymongoCon.insert_data(data)
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

    def start(self, tags=None):
        if tags is None:
            tags = []
        self.stream.filter(track=tags)

    def stop(self):
        self.stream.disconnect()


if __name__ == "__main__":

    listener = Listener()
    parser = argparse.ArgumentParser()
    parser.add_argument('-topics')
    args = parser.parse_args()
    aut = OAuthHandler(API_TOKEN, API_SECRET)
    aut.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = TwitterStream(aut, listener)
    stream.start(args.topics.split(","))
