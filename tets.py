from Conf import MONGO_DB, MONGO_PASSWORD, API_SECRET, API_TOKEN, ACCESS_TOKEN, ACCESS_SECRET
import tweepy

aut = tweepy.OAuthHandler(API_TOKEN, API_SECRET)
aut.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(aut)
print(api.update_status(status="hello").id)
