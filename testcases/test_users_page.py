import unittest
from testcases.base_test import BaseTest
from pageObjects.pages.login_page import LoginPage
from pageObjects.pages.users_page import UsersPage


class UsersTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.user_page = UsersPage(self.driver)

    @unittest.skip('https://zisoft.atlassian.net/browse/ZIS-233')
    def test01_create_new_user(self):
        """ ZST-005
        *Admin create new user*
        **Test Scenario:**
        #. Login as admin.
        #. Create new user, should succeed.
        #. Login as a new user, should succeed.
        """
        self.login_page.login_as_admin(username=self.login_page.admin_username,
                                       password=self.login_page.admin_password)
        username, password = self.user_page.create_new_user(role='User')
        self.assertTrue(self.login_page.login_as_user(username, password))

