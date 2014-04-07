from bobcraft.yubikey_creds import client_id, secret_key
from yubico_client import Yubico

class YubikeyFactor(object):
  prompt = "press yubikey button"

  def __init__(self, yubikey_id):
    self.yubikey_id = yubikey_id

  def start(self): pass

  def check_otp(self, otp):
    client = Yubico(client_id, secret_key)
    return (get_public_id(otp) == self.yubikey_id
            and client.verify(otp))

def get_public_id(otp):  # module level function
  return otp[:-32]
