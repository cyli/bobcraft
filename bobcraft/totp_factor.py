from os import urandom
from otpauth import OtpAuth

class TOTPFactor(object):
  prompt = "token?"

  def __init__(self, secret=None):
    self.secret = secret or urandom(40)

  def start(self): pass

  def check_otp(self, otp):
    otpa = OtpAuth(self.secret)
    return otpa.valid_totp(otp)
