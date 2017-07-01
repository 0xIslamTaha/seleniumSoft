import unittest
from pytractor import webdriver
from pageObjects.basePage.__init__ import CONFIG


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setUp(self):
        self.driver = self.set_browser()

    def tearDown(self):
        self.driver.quit()

    def set_browser(self):
        if CONFIG['browser'] == 'chrome':
            DRIVER = webdriver.Chrome()
        elif CONFIG['browser'] == 'firefox':
            DRIVER = webdriver.Firefox()
        elif CONFIG['browser'] == 'ie':
            DRIVER = webdriver.Ie()
        elif CONFIG['browser'] == 'opera':
            DRIVER = webdriver.Opera()
        elif CONFIG['browser'] == 'safari':
            DRIVER = webdriver.Safari
        else:
            print("Invalid browser configuration [%s]" % CONFIG['browser'])
        return DRIVER
