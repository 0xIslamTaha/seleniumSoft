import unittest
from framework.pages.userspage import UsersPage


class Users(UsersPage):
    @unittest.skip('https://zisoft.atlassian.net/browse/ZIS-233')
    def test01_create_new_user(self):
        """ ZST-005
        *Admin create new user*
        **Test Scenario:**
        #. Login as admin.
        #. Create new user, should succeed.
        #. Login as a new user, should succeed.
        """
        self.login_page.login_as_admin(username=self.admin_username,
                                       password=self.admin_password)
        username, password = self.create_new_user(role='User')
        self.assertTrue(self.login_page.login_as_user(username, password))

