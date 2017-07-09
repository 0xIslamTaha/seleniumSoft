from pageObjects.basePage.base_page import BasePage
from pageObjects.navigation.main_menu import MainMenu
import uuid


class PhishingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_menu = MainMenu(driver)

    def get_phishpot_page(self):
        pass

    def get_phishing_page(self):
        pass
