import unittest

try:
    from blue .user .signin import *
except ImportError:
    print("user package is not import !")


class SignTest(unittest.TestCase):
    """
    This class is just for testing of signin.py
    from user package

    """
    pass
