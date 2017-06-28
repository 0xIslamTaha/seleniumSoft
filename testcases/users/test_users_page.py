from framework.pages.userspage import UsersPage
from framework.pages.loginpage import LoginPage
from framework.navigation.main_menu import MainMenu


class Users(UsersPage):
    def __init__(self):
        super().__init__()
        self.login_page = LoginPage()
        self.main_menu = MainMenu()

    def test01_create_new_user(self):
        self.login_page.login_as_admin(username=self.admin_username,
                                       password=self.admin_password)
        self.assertTrue(self.main_menu.get_users_page(), "Can't get users page")
        self.click('users_action_button')
        self.click('click_manual')

