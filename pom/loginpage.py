
from Generic.XLUtils import read_locators

path = r"C:\Users\Admin\Desktop\A2_Selenium\HybridFramework\excel_files\locators.xlsx"
loc = read_locators(path,"loginpage")

# {'username_textfield': ['name', 'username']

# var[key]


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def username_textfield(self,un):
        self.driver.find_element(*loc['username_textfield']).send_keys(un)

    def password_textfield(self,pwd):
        self.driver.find_element(*loc['password_textfield']).send_keys(pwd)

    def login_btn(self):
        self.driver.find_element(*loc['login_button']).click()


    def forgot_password_link(self):
        ...

    def orange_link(self):
        ...