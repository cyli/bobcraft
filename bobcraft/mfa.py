from bobcraft.totp_factor import TOTPFactor
from bobcraft.sms_factor import SMSFactor
from bobcraft.yubikey_factor import YubikeyFactor, get_public_id
from bobcraft.made_up import get_user_input
from bobcraft.login import login

from otpauth import OtpAuth
import qrcode

from functools import partial


def add_totp(user):
  totp = TOTPFactor()
  qr_code = generate_qr_code(totp, user.username)

  totp_token = get_user_input(prompt=qr_code)

  if totp.check_otp(totp_token):
    user.possession_factors += (totp,)


def generate_qr_code(totp, username):
  otpa = OtpAuth(totp.secret)
  uri = otpa.to_uri(
    'totp', 'BobCraft:{0}'.format(username),
    'BobCraft')
  return qrcode.make(uri)


def add_sms(user):
  user_phone = get_user_input(prompt="phone #")
  sms = SMSFactor(user_phone)

  if sms not in user.possession_factors:
      sms.start()
      sms_token = get_user_input(prompt="token")

      if sms.check_otp(sms_token):
        user.possession_factors += (sms,)


def add_yubikey(user):
  otp = get_user_input(prompt="Yubikey OTP")

  yubikey = YubikeyFactor(get_public_id(otp))

  if (yubikey not in user.possession_factors and
      yubikey.check_otp(otp)):
    user.possession_factors += (yubikey,)


def remove_factor(user, factor):
  user.possession_factors = (
    f for f in user.possession_factors
    if f != factor)

  user.email("A factor has been removed", factor)


def secure_remove_factor(user, factor):
  password = get_user_input(prompt="password")

  login(user.username, password,
        partial(remove_factor, factor=factor))
