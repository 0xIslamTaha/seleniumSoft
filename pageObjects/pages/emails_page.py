from pageObjects.basePage.base_page import BasePage
from pageObjects.navigation.main_menu import MainMenu
import uuid


class EmailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_menu = MainMenu(driver)

    def get_email_serve_page(self):
        pass

    def get_email_template_page(self):
        pass

    def get_jobs_page(self):
        pass
