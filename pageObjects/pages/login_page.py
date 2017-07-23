from pageObjects.basePage.base_page import BasePage


class LoginPage(BasePage):
    def get_login_page(self):
        self.get_page(page_url=self.url)

    def login_as_admin(self, username, password):
        self.login(username, password)
        if self.check_element_is_exist(element='left_menu'):
            return True
        else:
            return False

    def login_as_user(self, username, password):
        try:
            self.login(username, password)
            self.find_element(element='home')
            return True
        except:
            return False

    def login(self, username, password):
        print(' [*] Log in as %s ' % username)
        self.get_login_page()
        if self.check_element_is_exist(element='username'):
            self.set_text(element='username', value=username)
            self.set_text(element='password', value=password)
            self.click(element='login')

    def logout(self):
        try:
            self.find_element('admin').click()
            self.find_element('logout').click()
            return True
        except:
            return False