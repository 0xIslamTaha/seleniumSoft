from framework.pages.loginpage import LoginPage
import uuid


class Login(LoginPage):
    def test01_login_as_admin(self):
        self.assertTrue(self.login_as_admin(username=self.admin_username,
                                            password=self.admin_password))

    def test02_login_with_wrong_username(self):
        username = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=username,
                                             password=self.admin_password))

    def test03_login_with_wrong_password(self):
        password = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=self.admin_username,
                                             password=password))

    def test04_login_with_wrong_username_wrong_password(self):
        username = str(uuid.uuid4())
        password = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=username,
                                             password=password))
