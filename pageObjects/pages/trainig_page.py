from pageObjects.basePage.base_page import BasePage
from pageObjects.navigation.main_menu import MainMenu


class TrainingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_menu = MainMenu(driver)

    def get_campaigns_page(self):
        return self.main_menu.get_campaigns_page()

    def add_new_campaign(self):
        self.get_campaigns_page()
        self.click('users_action_button')
        self.click('create_campaign')
        title = self.generate_random_string()
        self.set_text(element='title', value=title)
        self.select(list_element='exam', item_value='Default')
        self.click('save_campaign')
        return self.verify_data_in_table(data=title)
