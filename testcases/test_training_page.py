import unittest
from testcases.base_test import BaseTest
from pageObjects.pages.login_page import LoginPage
from pageObjects.pages.trainig_page import TrainingPage


class TrainingTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.training_page = TrainingPage(self.driver)

    def test01_create_new_campaign(self):
        """ ZST-006
        *Admin create new campaign*
        **Test Scenario:**
        #. Login as admin.
        #. Create new campaign, should succeed.
        """
        self.assertTrue(self.training_page.add_new_campaign())

