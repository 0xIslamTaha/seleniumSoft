from pageObjects.basePage.base_page import BasePage


class MainMenu(BasePage):
    def get_users_page(self):
        self.hover_over_element('users')
        users = self.find_elements('users')
        users[1].click()
        if 'users' in self.get_url():
            return True
        else:
            return False

    def get_campaigns_page(self):
        self.hover_over_element('training')
        self.click('campaigns')
        if 'campaigns' in self.get_url():
            return True
        else:
            return False

    def get_departments_page(self):
        self.hover_over_element('users')
        self.click('departments')
        if 'departments' in self.get_url():
            return True
        else:
            return False