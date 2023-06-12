# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import datetime

day = datetime.datetime.today().weekday()
print(day)

account_sid = "ACe0f26e6158438ffd7c1cea2b4f79b654"
auth_token = "67c9da3bfe7ab48ffc8f59ae2fee2514"
client = Client(account_sid, auth_token)
content = "Today is Monday" if day ==0 else '''...


I am getting tired baby...i love you so much. goodnight my queen <3 
'''
message = client.messages.create(
  body=content,
  from_="+18445310674",
  to="+13336669876")