"""
User model wth a fake user DB
"""

from __future__ import print_function

from bcrypt import hashpw, gensalt


class UserAlreadyExists(Exception):
    pass


class UserDB(object):
    """
    Fake in-memory user DB - not in slides
    """
    def __init__(self):
        self.pwd_db = {}
        self.factor_db = {}

    def add_user(self, username, password):
        if username in self.pwd_db:
            raise UserAlreadyExists(username)

        self.pwd_db[username] = hashpw(password, gensalt())
        self.factor_db[username] = ()


user_db = None


class User(object):
  """Represents a user account"""
  def __init__(self, username, _user_db=None):
    self.username = username
    self._user_db = _user_db or user_db

  @property
  def possession_factors(self):     # in preference order
    return self._user_db.factor_db.get(self.username, ())

  @possession_factors.setter
  def possession_factors(self, value):
    self._user_db.factor_db[self.username] = value

  def validate_password(self, pwd):
    """Validates the password against
    the stored hash"""
    hashed = self._user_db.pwd_db[self.username]
    return hashpw(pwd, hashed) == hashed

  def email(self, *message):
    """Emails the user"""
    print("Fake email user {0}".format(self.username),
          *message)
    print("\n")

  def exists(self):
    return self.username in self._user_db.pwd_db
