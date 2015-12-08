from Twython import Twython

TWITTER_APP_KEY = ''
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

t = Twython(app_key=TWITTER_APP_KEY, app_secret=TWITTER_APP_KEY_SECRET, oauth_token=TWITTER_ACCESS_TOKEN, oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#omg', count=100)

tweets = search['statuses']

for tweet in tweets:
print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
