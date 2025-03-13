
from src.test.TestCTFPage import TestCTFPage
from src.page.LoginPage import LoginPage
from src.data import User


class TestLoginPage(TestCTFPage):
    __testCases = [
        "\n" + "*** testCanLoginWithValidAccount ***",
        "\n" + "*** testCanNotLoginWithInValidAccount ***",
        "\n" + "*** testCanLogout ***",
    ]

    def _openLoginPage(self):
        return LoginPage(self.driver)

    def _openMainPage(self):
        loginPage = self._openLoginPage()
        return loginPage.login_with_valid_user(User.USERNAME, User.PASSWORD)

    def testCanLoginWithValidAccount(self):
        print(self.__testCases.__getitem__(0))
        self._openMainPage()

    def testCanNotLoginWithInValidAccount(self):
        print(self.__testCases.__getitem__(1))
        loginPage = self._openLoginPage()
        self.assertTrue(loginPage.login_with_in_valid_user("a", "123456"))

    def testCanLogout(self):
        print(self.__testCases.__getitem__(2))
        loginPage = self._openLoginPage()
        mainPage = loginPage.login_with_valid_user(User.USERNAME, User.PASSWORD)
        mainPage.logout()



        
    


