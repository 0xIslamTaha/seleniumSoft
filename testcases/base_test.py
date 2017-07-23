import unittest, random
from selenium import webdriver
from pageObjects.basePage.__init__ import CONFIG
from pageObjects.pages.login_page import LoginPage
import logging


class BaseTest(unittest.TestCase):
    DRIVER = None
    Logged_in = False

    logging.basicConfig(filename='log.log', filemode='rw', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('log.log')
    logger.addHandler(fileHandler)

    '''
    How to use:
        self.logger.debug("This is a debug message")
        self.logger.info("Informational message")
        self.logger.error("An error has happened!")
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = BaseTest.logger
        self.driver = self.set_browser()
        self.login_page = LoginPage(self.driver)

    def setUp(self):
        if not BaseTest.Logged_in:
            self.login_page.login_as_admin(username=self.login_page.admin_username,
                                           password=self.login_page.admin_password)
            BaseTest.Logged_in = True

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def set_browser():
        if not BaseTest.DRIVER:
            if CONFIG['browser'] == 'chrome':
                BaseTest.DRIVER = webdriver.Chrome()
            elif CONFIG['browser'] == 'firefox':
                BaseTest.DRIVER = webdriver.Firefox()
            elif CONFIG['browser'] == 'ie':
                BaseTest.DRIVER = webdriver.Ie()
            elif CONFIG['browser'] == 'opera':
                BaseTest.DRIVER = webdriver.Opera()
            elif CONFIG['browser'] == 'safari':
                BaseTest.DRIVER = webdriver.Safari
            else:
                print("Invalid browser configuration [%s]" % CONFIG['browser'])
        return BaseTest.DRIVER

    def generate_random_string(self):
        result = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(random.randint(0, len(chars))):
            result += random.choice(chars)
        return result
