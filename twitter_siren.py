from twython import Twython
import RPi.GPIO as GPIO

APP_KEY = 'UKCbxSI4r4ZEBKeEOnAXTSJhq'
APP_SECRET = 'Fj6pMAjEkZc9bsY3LGXwre1FN2xMK4ILKUNVTUymGKaaCFAkZt'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens(callback_url='http://mysite.com/callback')

OAUTH_TOKEN = auth['942231685-OLbeDiZSRGgH5fACG0JyOGEDMpEu9hhhFYs76opT']
OAUTH_TOKEN_SECRET = auth['YYxrTuDzJoaG6O3WUCWAzdiotfOT4fQmmvUtJ5wlE7MM6']

results = twitter.search(q='legacymarketing')

total = 0

def counter(results):
    for i in results:
        total = total + i
    return total
    if total >= 150:
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)


