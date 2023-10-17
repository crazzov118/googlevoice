import pprint
from googlevoice import Voice

print("This is google voice api test")
voice = Voice()
voice.login()

outgoingNumber = input('Number to call: ')
forwardingNumber = input('Number to call from [optional]: ') or None

voice.call(outgoingNumber, forwardingNumber)

if input('Calling now... cancel?[y/N] ').lower() == 'y':
    voice.cancel(outgoingNumber, forwardingNumber)
