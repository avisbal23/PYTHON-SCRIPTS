from twilio.rest import Client
accountSID = 'ACe0f26e6158438ffd7c1cea2b4f79b654'
authToken = '320201e44ff54d3723e29481254fc8ad'
myTwilioNumber = "+18445310674"
myCellPhone = "+16786659558"

client = Client(accountSID, authToken)
message = client.messages.create(
  body="Yo yo yo!",
  from_=myTwilioNumber,
  to=myCellPhone
)
