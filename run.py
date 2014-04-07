"""
A toy app demonstrating 2-factor auth
"""

from __future__ import print_function
import getpass
import sys

from bobcraft import mfa, user
from bobcraft.login import login
from bobcraft.made_up import get_user_choice


class ToyApplication(object):

    def __init__(self):
        self.user_db = user.user_db = user.UserDB()

    def dispatch(self, text, *args):
        method_name = text.lower().strip().replace(' ', '_')
        method = getattr(self, method_name)
        return method(*args)

    def quit(self):
        sys.exit()

    def start(self):
        options = ("Add user", "Select user", "Quit")
        choice = get_user_choice(options)
        self.dispatch(choice)

    def add_user(self):
        while True:
            username = raw_input("username: ")
            if username.strip():
                password = getpass.getpass("password: ")

                try:
                    self.user_db.add_user(username, password)
                except user.UserAlreadyExists:
                    print("User already exists.\n")
                else:
                    return self.start()
            else:
                print("Username cannot be blank.\n")

    def select_user(self, *args):
        options = self.user_db.pwd_db.keys()
        options.append("Back to start")
        options.append("Quit")

        choice = get_user_choice(options)
        if choice == "Back to start":
            choice = "Start"

        if choice in ("Start", "Quit"):
            self.dispatch(choice)
        else:
            self.user_screen(choice)

    def user_screen(self, username):
        options = ("Login", "Add factor", "Remove factor", "Back to Select User")
        choice = get_user_choice(options)
        if choice == "Back to Select User":
            choice = "Select user"

        self.dispatch(choice, username)

    def login(self, username):
        password = getpass.getpass("password: ")

        def post_login(usr):
            print("{0} logged in successfully!\n".format(usr.username))
            self.user_screen(usr.username)

        try:
            login(username, password, post_login)
        except:
            print("Invalid login credentials\n")
            self.user_screen(username)

    def add_factor(self, username):
        options = ("TOTP", "SMS", "Yubikey", "Cancel")
        choice = get_user_choice(options)
        if choice == "Cancel":
            return self.user_screen(username)

        usr = user.User(username, self.user_db)
        method = getattr(mfa, "add_{0}".format(choice.lower()))
        method(usr)
        self.user_screen(username)

    def remove_factor(self, username):
        usr = user.User(username, self.user_db)
        options = list(usr.possession_factors) + ["Cancel"]
        choice = get_user_choice(options)
        if choice == "Cancel":
            return self.user_screen(username)

        print("Please enter credentials to remove factor:\n")
        try:
            mfa.secure_remove_factor(usr, choice)
        except:
            print("Unable to remove factor due to invalid login credentials\n")
        self.user_screen(username)


if __name__ == "__main__":
    app = ToyApplication()
    app.start()
