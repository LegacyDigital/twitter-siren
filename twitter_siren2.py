from twython import Twython
import RPi.GPIO as GPIO

TWITTER_APP_KEY = 'UKCbxSI4r4ZEBKeEOnAXTSJhq'
TWITTER_APP_KEY_SECRET = 'Fj6pMAjEkZc9bsY3LGXwre1FN2xMK4ILKUNVTUymGKaaCFAkZt'
TWITTER_ACCESS_TOKEN = '942231685-OLbeDiZSRGgH5fACG0JyOGEDMpEu9hhhFYs76opT'
TWITTER_ACCESS_TOKEN_SECRET = 'YYxrTuDzJoaG6O3WUCWAzdiotfOT4fQmmvUtJ5wlE7MM6'

t = Twython(app_key=TWITTER_APP_KEY, app_secret=TWITTER_APP_KEY_SECRET, oauth_token=TWITTER_ACCESS_TOKEN, oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#legacymarketing', count=151)

tweets = search['statuses']

# for tweet in tweets:
#     print tweet['id_str'], '\n', tweet['text'], '\n\n\n'

tweets = []

for i in search:
    tweets.append([i])
    length = len(tweets)
    print length
    if length >= 150:
        print "Siren!"
        GPIO.output(18, True)
        time.sleep(1000)
        GPIO.output(18, False)
    else:
        print "No siren."
        GPIO.output(18, False)
