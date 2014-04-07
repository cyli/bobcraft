from bobcraft.twilio_creds import account_sid, auth_token, from_number
from twilio.rest import TwilioRestClient


class SMSFactor(object):
  prompt = "code from text?"

  def __init__(self, user_phone):
    self.user_phone = user_phone
    self.stored = None
    self.client = TwilioRestClient(account_sid, auth_token)

  def start(self):
    from random import SystemRandom
    self.stored = SystemRandom().randint(1, 999999)
    self.client.sms.messages.create(
      body=str(self.stored),
      to=self.user_phone, from_=from_number)

  def check_otp(self, otp):
    return int(otp) == self.stored
