import time, random
import unittest
import logging
from testconfig import config
from pytractor import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.basePage.__init__ import CONFIG
from pageObjects.basePage.elements import elements


class BasePage:
    def __init__(self, driver):
        self.url = CONFIG['url']
        self.admin_username = CONFIG['admin_username']
        self.admin_password = CONFIG['admin_password']
        self.user_username = CONFIG['admin_username']
        self.user_password = CONFIG['user_password']
        self.browser = CONFIG['browser']
        self.elements = elements
        self.session = CONFIG['session']
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def lg(self, msg):
        pass

    def wait_until_element_located(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        for temp in range(3):
            try:
                self.wait.until(EC.visibility_of_element_located((getattr(By, method), value)))
                return True
            except:
                time.sleep(1)
        else:
            return False

    def find_elements(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        if method in ['XPATH', 'ID', 'LINK_TEXT', 'CLASS_NAME', 'NAME', 'TAG_NAME']:
            elements_value = self.driver.find_elements(getattr(By, method), value)
        else:
            self.fail("This %s method isn't defined" % method)
        return elements_value

    def find_element(self, element):
        method = self.elements[element][0]
        value = self.elements[element][1]
        # if method in ['XPATH', 'ID', 'LINK_TEXT']:
        element_value = self.driver.find_element(getattr(By, method), value)
        # elif method in ['CLASS_NAME', 'NAME', 'TAG_NAME']:
        #     item_order = self.elements[element][2]
        #     elements_value = self.driver.find_elements(getattr(By, method), value)
        #     if item_order == -1:
        #         element_value = elements_value
        #     else:
        #         element_value = elements_value[item_order]
        # else:
        #     self.fail("This %s method isn't defined" % method)
        return element_value

    def get_page(self, page_url):
        try:
            self.driver.get(page_url)
        except Exception as e:
            self.lg(' * %s Exception at get_page(%s) ' % (str(e), page_url))
        else:
            self.execute_angular_script()
            self.maximize_window()

    def click(self, element):
        for temp in range(10):
            try:
                self.find_element(element).click()
                break
            except:
                time.sleep(1)
        else:
            self.fail("can't find %s element" % element)
        time.sleep(1)

    def click_link(self, link):
        self.get_page(link)

    def get_text(self, element):
        for temp in range(10):
            try:
                return self.find_element(element).text
            except:
                time.sleep(0.5)
        else:
            self.fail('NoSuchElementException(%s)' % element)

    def get_value(self, element):
        return self.get_attribute(element, "value")

    def element_link(self, element):
        return self.get_attribute(element, "href")

    def get_attribute(self, element, attribute):
        self.wait_until_element_located(element)
        return self.find_element(element).get_attribute(attribute)

    def get_url(self):
        try:
            curent_url = self.driver.current_url
            self.driver.ignore_synchronization = False
        except:
            self.driver.ignore_synchronization = True
            curent_url = self.driver.current_url
        return curent_url

    def set_text(self, element, value):
        self.wait_until_element_located(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(value)

    def clear_text(self, element):
        self.wait_until_element_located(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(Keys.ENTER)

    def clear_element_text(self, element):
        element.clear()
        element.send_keys(Keys.ENTER)

    def clear_text_columns(self, element, ID):
        method = self.elements[element][0]
        value = self.elements[element][1] % ID
        time.sleep(1)
        try:
            element_value = self.driver.find_element(getattr(By, method), value)
            element_value.clear()
            element_value.send_keys(Keys.ENTER)
            return True
        except:
            self.lg("can't find element")
            return False

    def move_curser_to_element(self, element):
        element = self.elements[element]
        location = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, element)))
        ActionChains(self.driver).move_to_element(location).perform()

    def wait_element(self, element):
        if self.wait_until_element_located(element):
            return True
        else:
            return False

    def check_element_is_exist(self, element):
        if self.wait_element(element):
            return True
        else:
            return False

    def select(self, list_element, item_value):
        item_value = str(item_value)
        self.select_obeject = Select(self.find_element(list_element))
        self.select_list = self.select_obeject.options

        for option in self.select_list:
            if item_value in option.text:
                self.lg("select %s from list" % str(option.text))
                self.select_obeject.select_by_visible_text(option.text)
                item_value = option.text
                break
        else:
            self.fail("This %s item isn't an option in %s list" % (item_value, list_element))

    def get_list_items(self, list_element):
        html_list = self.find_element(list_element)
        return html_list.find_elements_by_tag_name("li")

    def get_list_items_text(self, list_element):
        compo_menu = self.get_list_items(list_element)
        compo_menu_exist = []
        for item in compo_menu:
            if item.text != "":
                if '\n' in item.text:
                    data = item.text.split('\n')
                    compo_menu_exist += data
                else:
                    compo_menu_exist.append(item.text)
        return compo_menu_exist

    def element_in_url(self, text_item):
        if " " in text_item:
            text_item = text_item.replace(" ", "%20")
        for temp in range(10):
            try:
                if text_item in self.get_url():
                    return True
            except:
                time.sleep(1)
        else:
            self.fail("this %s item isn't exist in this url: %s" % (text_item, self.get_url()))

    def maximize_window(self):
        time.sleep(1)
        screen_dimention = self.driver.get_window_size()
        screen_size = screen_dimention['width'] * screen_dimention['height']
        if screen_size < 1800 * 1000:
            self.driver.set_window_size(1800, 1000)

    def execute_angular_script(self):
        # This method is trying to load angular elements.
        for _ in range(30):
            if self.driver.title:
                return True
            else:
                time.sleep(2)
                try:
                    self.driver.execute_script('angular.resumeBootstrap();')
                    time.sleep(2)
                except Exception as e:
                    self.lg(' * Exception : %s ' % str(e))

    def hover_over_element(self, element):
        element_to_hover_over = self.find_element(element=element)
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()

    def generate_random_string(self):
        result = ''
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(random.randint(0, len(chars))):
            result += random.choice(chars)
        return result
