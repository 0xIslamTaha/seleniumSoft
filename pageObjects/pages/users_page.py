from pageObjects.basePage.base_page import BasePage
from pageObjects.navigation.main_menu import MainMenu
import uuid, random


class UsersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_menu = MainMenu(driver)
        self.add_users_elements = ['firstName', 'lastName', 'username_', 'email', 'role', 'language',
                                   'default_campaign', 'password_', 'password_2', 'department', 'status']

    def get_users_page(self):
        if 'users' not in self.get_url():
            return self.main_menu.get_users_page()

    def create_new_user(self, role=''):
        print(' [*] Create new user.')
        if not role:
            role = random.choice(['Administrator', 'Superuser (Not Used)', 'User'])
        firstname = self.generate_random_string()
        lastname = self.generate_random_string()
        username = str(uuid.uuid4()).split('-')[0]
        password = str(uuid.uuid4()) + 'xTermX'
        self.get_users_page()
        self.click('users_action_button')
        self.click('add_user')
        self.set_text(element='firstName', value=firstname)
        self.set_text(element='lastName', value=lastname)
        self.set_text(element='username_', value=username)
        self.set_text(element='email', value=username + '@gmail.com')
        self.select(list_element='role', item_value=role)
        self.select(list_element='language', item_value='English')
        self.select(list_element='default_campaign', item_value='All Lessons (en)')
        self.click(element='reset')
        self.set_text(element='password_', value=password)
        self.set_text(element='password_2', value=password)
        self.select(list_element='department', item_value='Default')
        self.select(list_element='status', item_value='Enabled')
        self.click('save_user')
        print(' [*] New user : %s' % username)
        return username, password

    def search_for_user(self, username):
        self.get_users_page()
        return self.search_for(data=username, table_div_element='table_users_filter')

    def edit_user(self, user='', **kwargs):
        if not user:
            users = self.get_table_element_data()
            user = random.choice(users)
        self.search_for_user(username=user)
        self.click('edit_user')
        for key in kwargs:
            if key == 'firstName':
                self.set_text(element='firstName', value=kwargs[key])
            if key == 'lastName':
                self.set_text(element='firstName', value=kwargs[key])
            if key == 'username_':
                self.set_text(element='username_', value=kwargs[key])
            if key == 'email':
                self.set_text(element='email', value=kwargs[key])
            if key == 'role':
                self.select(list_element='role', item_value=kwargs[key])
            if key == 'language':
                self.select(list_element='language', item_value=kwargs[key])
            if key == 'default_campaign':
                self.select(list_element='default_campaign', item_value=kwargs[key])
            if key == 'password_':
                self.click(element='reset')
                self.set_text(element='password_', value=kwargs[key])
                self.set_text(element='password_2', value=kwargs[key])
            if key == 'department':
                self.select(list_element='department', item_value=kwargs[key])
            if key == 'status':
                self.select(list_element='status', item_value=kwargs[key])
        self.click('save_user')

    def get_edit_user_data(self, username):
        data = {}
        if self.search_for_user(username=username):
            for element in self.add_users_elements:
                data[element] = self.get_text(element=element)
        else:
            print(" [*] %s user isn't exist" % username)
            return False
        return data

    def delete_user(self, username=''):
        if self.search_for_user(username=username):
            self.click(element='delete_user')
            import ipdb; ipdb.set_trace()
            self.click(element='ok_btn')
        return not self.search_for_user(username=username)

    def get_departments_page(self):
        if 'departments' not in self.get_url():
            return self.main_menu.get_departments_page()

    def create_new_department(self):
        title = self.generate_random_string()
        self.get_departments_page()
        self.click('users_action_button')
        self.click('click_department')
        self.set_text(element='title', value=title)
        self.submit(element=title)
        return title

    def search_for_department(self, department):
        self.get_departments_page()
        return self.search_for(data=department, table_div_element='table_departments_filter')

    def edit_department(self):
        pass

    def add_users_to_department(self):
        pass

    def delete_department(self):
        pass

    def get_ldap_server_page(self):
        pass

    def create_new_ldap_server(self):
        pass

    def seach_for_ldap(self):
        pass

    def edit_ldap_server(self):
        pass
