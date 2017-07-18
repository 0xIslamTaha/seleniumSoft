import unittest, random
from selenium import webdriver
from pageObjects.basePage.__init__ import CONFIG


class BaseTest(unittest.TestCase):
    DRIVER = ''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.driver = self.set_browser()

    def tearDown(self):
        self.driver.quit()

    def set_browser(self):
        if CONFIG['browser'] == 'chrome':
            self.DRIVER = webdriver.Chrome()
        elif CONFIG['browser'] == 'firefox':
            self.DRIVER = webdriver.Firefox()
        elif CONFIG['browser'] == 'ie':
            self.DRIVER = webdriver.Ie()
        elif CONFIG['browser'] == 'opera':
            self.DRIVER = webdriver.Opera()
        elif CONFIG['browser'] == 'safari':
            self.DRIVER = webdriver.Safari
        else:
            print("Invalid browser configuration [%s]" % CONFIG['browser'])
        return self.DRIVER

    def generate_random_string(self):
        result = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(random.randint(0, len(chars))):
            result += random.choice(chars)
        return result