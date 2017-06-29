from framework.pages.loginpage import LoginPage
import uuid


class Login(LoginPage):
    def test01_login_as_admin(self):
        """ ZST-001
        *Test login as admin*
        **Test Scenario:**
        #. Login using correct credential, should succeed
        """
        self.assertTrue(self.login_as_admin(username=self.admin_username,
                                            password=self.admin_password))

    def test02_login_with_wrong_username(self):
        """ ZST-002
        *Test login with wrong username*
        **Test Scenario:**
        #. Login using wrong username, should fail
        """
        username = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=username,
                                             password=self.admin_password))

    def test03_login_with_wrong_password(self):
        """ ZST-003
        *Test login with wrong password*
        **Test Scenario:**
        #. Login using wrong password, should fail
        """
        password = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=self.admin_username,
                                             password=password))

    def test04_login_with_wrong_username_wrong_password(self):
        """ ZST-004
        *Test login with wrong username and wrong password*
        **Test Scenario:**
        #. Login using wrong username and wrong password, should fail
        """
        username = str(uuid.uuid4())
        password = str(uuid.uuid4())
        self.assertFalse(self.login_as_admin(username=username,
                                             password=password))
