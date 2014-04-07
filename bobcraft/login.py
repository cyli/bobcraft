from bobcraft.user import User
from bobcraft.made_up import get_user_input
from bobcraft.made_up import get_user_choice


class InvalidLogin(Exception):
    pass


def login(username, password, post_login):
  user = User(username)
  if (user.exists() and
      user.validate_password(password) and
      check_possession_factor(user)):
    post_login(user)
  else:
    raise InvalidLogin(username)


# The basic check_possession_factor that only checks the prefered factor
#
# def check_possession_factor(user):
#   if len(user.possession_factors) == 0:
#     return True

#   factor = user.possession_factors[0]
#   factor.start()
#   otp = get_user_input(prompt=factor.prompt)
#   return factor.check_otp(otp)


def check_possession_factor(user):
  if len(user.possession_factors) == 0:
    return True

  factor = get_user_choice(user.possession_factors)
  factor.start()
  otp = get_user_input(prompt=factor.prompt)

  if factor != user.possession_factors[0]:
    user.email("Login with backup factor", factor)

  return factor.check_otp(otp)
