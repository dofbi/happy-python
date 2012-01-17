import random
from time import sleep
import os

from tweepy import *

consumer_key = 'KEY'
consumer_secret = 'SECRET'

auth = OAuthHandler(consumer_key, consumer_secret)
  
auth_url = auth.get_authorization_url()
print 'Autoriser: ' + auth_url
verifier = raw_input('PIN: ').strip()

access_token = auth.get_access_token(verifier)


api = API(auth)

for follower in Cursor(api.friends).items():
  utilisateur = follower.screen_name
  print utilisateur
  api.update_status('D @%s 2012 !!! Tous mes meilleurs voeux, happy new year ;-)' %utilisateur )
  sleep(35)
