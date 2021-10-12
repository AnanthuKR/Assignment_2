import pymongo


class PyMongoConnection:
    def __init__(self, password, db):
        client = pymongo.MongoClient(
            "mongo DB connection string".format(password, db))
        self.db = client.Twitter_Data
        self.coll = self.db.tweets

    def insert_data(self, tweet_data):
        if isinstance(tweet_data, list):
            self.coll.insert_many(tweet_data)
