import pymongo


class PyMongoConnection:
    def __init__(self, password, db):
        client = pymongo.MongoClient(
            "mongodb+srv://ananthu329:{0}@litest001.ny9ap.mongodb.net/{1}?retryWrites=true&w=majority".format(password,
                                                                                                              db))
        self.db = client.Twitter_Data
        self.coll = self.db.tweets

    def insert_data(self, tweet_data):
        if isinstance(tweet_data, list):
            self.coll.insert_many(tweet_data)

    def get_data(self):
        return self.coll.find().sort("InsertedAt")
