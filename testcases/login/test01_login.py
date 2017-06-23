from framework.pages.loginpage import LoginPage


class Login(LoginPage):
    def test01_login_as_admin(self):
        self.assertTrue(self.login_as_admin())

