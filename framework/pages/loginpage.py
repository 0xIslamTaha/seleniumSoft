from framework.utiles.utiles import BaseTest


class LoginPage(BaseTest):
    def get_login_page(self):
        self.get_page(page_url=self.url)

    def login_as_admin(self):
        self.get_login_page()
        self.set_text(element='username', value=self.admin_username)
        self.set_text(element='password', value=self.admin_password)
        self.find_element(element='password').submit()
        try:
            self.find_element(element='admin_setting')
            return True
        except:
            return False
