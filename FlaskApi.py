from flask import Flask, jsonify
from MongoDB import PyMongoConnection
from Conf import MONGO_DB, MONGO_PASSWORD, API_SECRET, API_TOKEN, ACCESS_TOKEN, ACCESS_SECRET
import tweepy
import datetime

mongoConn = PyMongoConnection(password=MONGO_PASSWORD, db=MONGO_DB)
aut = tweepy.OAuthHandler(API_TOKEN, API_SECRET)
aut.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(aut)

app = Flask(__name__)


@app.route('/tweets')
def get_tweets():
    datas = mongoConn.get_data()
    data_lis = []
    for data in datas:
        data.pop('_id')
        data_lis.append(data)

    return jsonify(sorted(data_lis, key=lambda x: x.get("insertedAt"), reverse=True))


@app.route("/addtweets/<text>")
def add_tweet(text):

    tweet = api.update_status(status=text)
    data = {
        "t_id": tweet.id,
        "insertedAt": datetime.datetime.now(),
        "createdAt": tweet.created_at,
        "text": text,
        'likes': 0,
        "profile_url": api.me().profile_image_url,
        "user_id": api.me().id,
        "user_name": api.me().name,
    }

    mongoConn.insert_data([data])

    datas = mongoConn.get_data()
    data_lis = []
    for data in datas:
        data.pop('_id')
        data_lis.append(data)

    return jsonify(sorted(data_lis, key=lambda x: x.get("insertedAt"), reverse=True))


if __name__ == '__main__':
    app.run(debug=True)
