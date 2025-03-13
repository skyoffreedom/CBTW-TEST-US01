import sys
import unittest

from src.data import Settings, User
from src.test.TestLoginPage import TestLoginPage
from src.utils import Constants


def suite():
    suite = unittest.TestSuite()

    if True:
        # Login Page
        suite.addTest(TestLoginPage('testCanLoginWithValidAccount'))
        suite.addTest(TestLoginPage('testCanNotLoginWithInValidAccount'))
        suite.addTest(TestLoginPage('testCanLogout'))

    return suite


if __name__ == '__main__':
    if len(sys.argv) == 7:
        Constants.END_POINT = sys.argv[1]
        Settings.HIDE_UI    = True if sys.argv[2].lower() == 'true' else False
        User.USERNAME       = sys.argv[3]
        User.PASSWORD       = sys.argv[4]
        User.ROLE           = sys.argv[5]
        Settings.IMPORT_TYPE    = int(sys.argv[6])

    runner = unittest.TextTestRunner()
    result = runner.run(suite())
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
