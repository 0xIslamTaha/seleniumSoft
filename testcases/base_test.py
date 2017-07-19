import unittest, random
from selenium import webdriver
from pageObjects.basePage.__init__ import CONFIG


class BaseTest(unittest.TestCase):
    DRIVER = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.driver = self.set_browser()

    def tearDown(self):
        self.driver.quit()

    def set_browser(self):
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
