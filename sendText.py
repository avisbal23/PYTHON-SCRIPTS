#pip install --user --upgrade twilio 
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

#Set Credentials
account_sid = "ACe0f26e6158438ffd7c1cea2b4f79b654"
auth_token = "67c9da3bfe7ab48ffc8f59ae2fee2514"

# create message client object 
client = Client(account_sid, auth_token)

# Set message content 
smsContent = '''...

I'm getting tired baby, I love you...so much...
Te amo con todo mi corazon!
good night '''

# Send message 
message = client.messages.create(
  body=smsContent,
  from_="+18445310674",
  to="+16786659558"
)