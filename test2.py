
def sendMessage(text):
    from twilio.rest import TwilioRestClient

    account_sid = "ACa24e9362ab140f534eb0adfacc8f00f7" # Your Account SID from www.twilio.com/console
    auth_token  = "29b589a68ae1bcf6d9a15f65682827ba"  # Your Auth Token from www.twilio.com/console

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=text,
        to="+16462581332",    # Replace with your phone number
        from_="+19179245543") # Replace with your Twilio number

    print(message.sid)

from random import randint

x = randint(1,6);

if x == 1:
    text = 'You are wonderful';
elif x == 2:
    text = 'You are kind';
elif x == 3:
    text = 'You are sweet';
elif x == 4:
    text = 'You are nice';
elif x == 5:
    text = 'You are really cool';
else:
    text = 'YOU SUCK'

sendMessage(text);
