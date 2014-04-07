"""
World of Bobcraft ways to input data.  In the slides, none of these methods were
ever implemented but they were imported as part of the implementation of adding
factors (see ``mfa.py``)
"""
from __future__ import print_function

from qrcode.image.pil import PilImage

import random
import string


def get_user_input(prompt):
    if isinstance(prompt, PilImage):
        filename = "".join(random.choice(string.ascii_letters) for _ in xrange(10))
        filename = '/tmp/{0}'.format(filename)
        prompt.save(filename)
        return raw_input('generate TOTP from {0} and enter token: '.format(filename))

    if isinstance(prompt, basestring):
        return raw_input('{0}: '.format(prompt))


def get_user_choice(choices):
    options = ["{n}. {txt}".format(n=(n + 1), txt=repr(val)) for n, val in enumerate(choices)]
    prompt = "{0}\n\nEnter the number of your choice [default 1]: ".format('\n'.join(options))

    while True:
        num = raw_input(prompt)
        try:
            num = int(num)
        except:
            pass
        else:
            if num > 0 and num <= len(choices):
                return choices[num - 1]

        print("Invalid choice.\n")
