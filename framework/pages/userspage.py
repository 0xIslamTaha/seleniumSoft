from framework.utiles.utiles import BaseTest
from framework.navigation.main_menu import MainMenu

class UsersPage(BaseTest):
    def __init__(self):
        super().__init__()
        self.main_menu = MainMenu()

    def get_users_page(self):
        return self.main_menu.get_users_page()

