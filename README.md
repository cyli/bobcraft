This repository is a toy application contains all the example code used in the multifactor-from-scratch part of the World of BobCraft slides.

It also includes a little command-line runner that demos adding a user, adding a factor/removing a factor from a user's account, and logging in.  The `made_up` module from the slides, for which no implementation was ever provided, is actually implemented here.

The `user.py` module, particularly the `User` class, has changed a little to accomodate saving the user information somewhere.  However, it was presented on the slides as an interface.

The rest of the code is consistent with the slides.  This code does not do any error handling, nor is the factor collection abstraction ideal, nor does it provide enough feedback as to what is going on.

But purpose of structuring everything this way, was to make individual bits fit well onto slides rather than to actually have a full-featured and solid implementation.

So everything is pretty simple, if limited, but should hopefully be easy to understand.

To run the toy app:

- `pip install -r requirements.txt`
- Add Twilio credentials to `bobcraft/twilio_creds.py` [[sign up for a trial account](https://www.twilio.com/try-twilio)]
- Add a Yubico client ID and api key to `bobcraft/yubikey_creds.py` [[generate a key](https://upgrade.yubico.com/getapikey/)]
- `python run.py`
