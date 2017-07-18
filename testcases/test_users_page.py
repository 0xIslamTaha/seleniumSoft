import unittest, random, uuid
from testcases.base_test import BaseTest
from pageObjects.pages.login_page import LoginPage
from pageObjects.pages.users_page import UsersPage


class UsersTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)
        self.user_page = UsersPage(self.driver)
        self.login_page.login_as_admin(username=self.login_page.admin_username,
                                       password=self.login_page.admin_password)
        self.username, self.password = self.user_page.create_new_user()

    def tearDown(self):
        # self.user_page.delete_user(username=self.username)
        super().tearDown()

    def test01_create_new_user(self):
        """ ZST-005
        *Admin create new user*
        **Test Scenario:**
        #. Login as admin.
        #. Create new user, should succeed.
        #. Login as a new user, should succeed.
        """
        self.assertTrue(self.user_page.search_for_user(username=self.username), "FAIL : Create new user")

    @unittest.skip('https://github.com/islamTaha12/seleniumSoft/issues/2')
    def test02_delete_user(self):
        """ ZST-006
        **
        **Test Scenario:**
        #. Login as admin.
        #. Create new user
        #. Delete this user
        """
        self.assertTrue(self.user_page.delete_user(username=self.username))

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

        original_data = {'firstName': self.generate_random_string(),
                         'lastName': self.generate_random_string(),
                         'username_': self.generate_random_string(),
                         'email': self.generate_random_string()+"@gmail.com",
                         'role': random.choice['Administrator', 'Superuser (Not Used)', 'User'],
                         'language': random.choice['English', 'Arabic'],
                         'default_campaign': random.choice['All Lessons (ar)', 'All Lessons (en)'],
                         'password_': str(uuid.uuid4())+'xTreMx',
                         'status': random.choice['Enabled', 'Disabled']}
        self.user_page.edit_user(user=self.username, firstName=original_data['firstName'],
                                 lastName=original_data['lastName'], username_=original_data['username_'],
                                 email=original_data['email'], role=original_data['role'],
                                 language=original_data['language'], default_campaign=original_data['default_campaign'],
                                 password_=original_data['password_'], status=original_data['status'])
        new_data = self.user_page.get_edit_user_data(username=self.username)
        for key in new_data:
            if key in original_data.keys():
                self.assertEqual(new_data[key], original_data[key], " [*] Edit user page has a bug.")

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
        import ipdb;
        ipdb.set_trace()
