from django.conf import settings
from .melipayamak import Api

def send_verification_code(phone_number, code):
    username = settings.SMS_API['username']
    password = settings.SMS_API['password']
    api = Api(username,password)
    sms = api.sms()
    to = str(phone_number)
    text = code
    bodyId = settings.SMS_API['bodyId']
    response = sms.send_by_base_number(text, to, bodyId)
    if response['RetStatus'] == 1:
        return True
    else:
        # Handle errors
        return False
