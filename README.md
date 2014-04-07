This repository contains all the code used in the multifactor-from-scratch part of the World of BobCraft slides.

The user model and DB are a little changed, but the rest of the code is consistent with the slides.

It also includes a little command-line runner that demos adding a user, adding a factor/removing a factor from a user's account, and logging in.

This code does not deal with error conditions in the Twilio and Yubikey API's, the command line interface reports insufficient information, and it is not ideally factored.

The purpose of the structure of the code was to make individual bits fit well onto slides, so everything is pretty simple, but should hopefully be easy to understand.

To use:

- `pip install -r requirements.txt`
- Add Twilio credentials to `bobcraft/twilio_creds.py` [[sign up for a trial account](https://www.twilio.com/try-twilio)]
- Add a Yubico client ID and api key to `bobcraft/yubikey_creds.py` [[generate a key](https://upgrade.yubico.com/getapikey/)]
- `python run.py`
