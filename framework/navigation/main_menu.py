from framework.utiles.utiles import BaseTest


class MainMenu:
    def __init__(self):
        self.base_test = BaseTest()

    def get_users_page(self):
        self.base_test.hover_over_element('users')
        users = self.base_test.find_elements('users')
        users[1].click()
        if 'users' in self.base_test.get_url():
            return True
        else:
            return False
