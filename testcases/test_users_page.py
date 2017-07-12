import unittest
from testcases.base_test import BaseTest
from pageObjects.pages.login_page import LoginPage
from pageObjects.pages.users_page import UsersPage


class UsersTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.user_page = UsersPage(self.driver)

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
        self.assertTrue(self.login_page.login_as_user(username, password), "FAIL : Create new user")

    def test02_delete_user(self):
        """ ZST-006
        **
        **Test Scenario:**
        #. Login as admin.
        """
        pass

    def test08_edit_user(self):
        """ ZST-008
        *Admin edit an existing user*
        **Test Scenario:**
        #. Login as admin.
        #. Get users page, should succeed
        """
        self.login_page.login_as_admin(username=self.login_page.admin_username,
                                       password=self.login_page.admin_password)
        self.user_page.get_users_page()
        self.user_page.edit_user()
        import ipdb; ipdb.set_trace()
        # Edit username

    def test03_create_new_departments(self):
        """ ZST-007
        *Admin create new department*
        **Test Scenario:**
        #. Login as admin.
        #. Create new department, should succeed.
        """
        self.login_page.login_as_admin(username=self.login_page.admin_username,
                                       password=self.login_page.admin_password)
        self.user_page.get_departments_page()
        import ipdb; ipdb.set_trace()
