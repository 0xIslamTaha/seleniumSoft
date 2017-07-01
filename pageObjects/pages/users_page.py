from pageObjects.basePage.base_page import BasePage
from pageObjects.navigation.main_menu import MainMenu
import uuid


class UsersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_menu = MainMenu(driver)

    def get_users_page(self):
        return self.main_menu.get_users_page()

    def create_new_user(self, role):
        firstname = self.generate_random_string()
        lastname = self.generate_random_string()

        username = str(uuid.uuid4()).split('-')[0]
        password = str(uuid.uuid4()).split('-')[0]

        self.get_users_page()
        self.click('users_action_button')
        self.click('add_user')
        self.set_text(element='firstName', value=firstname)
        self.set_text(element='lastName', value=lastname)
        self.set_text(element='username_', value=username)
        self.set_text(element='email', value=username + '@gmail.com')
        self.select(list_element='role', item_value=role)
        self.select(list_element='language', item_value='English')
        self.click(element='reset')
        self.set_text(element='password_', value=password)
        self.set_text(element='password_2', value=password)
        self.select(list_element='department', item_value='Default')
        self.select(list_element='status', item_value='Enabled')
        self.click('save_user')
        return username, password
