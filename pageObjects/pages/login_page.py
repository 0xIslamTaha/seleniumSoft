from pageObjects.basePage.base_page import BasePage


class LoginPage(BasePage):
    def get_login_page(self):
        self.get_page(page_url=self.url)

    def login_as_admin(self, username, password):
        self.login(username, password)
        try:
            self.find_element(element='admin_setting')
            return True
        except:
            return False

    def login_as_user(self, username, password):
        try:
            self.login(username, password)
            self.find_element(element='home')
            return True
        except:
            return False

    def login(self, username, password):
        self.get_login_page()
        self.logout()
        self.set_text(element='username', value=username)
        self.set_text(element='password', value=password)
        self.find_element(element='password').submit()

    def logout(self):
        try:
            self.find_element('admin').click()
            self.find_element('logout').click()
            return True
        except:
            return False