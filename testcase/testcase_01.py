
from pom.loginpage import LoginPage
import time


def test_01(setup):
    driver = setup
    login_obj = LoginPage(driver)
    login_obj.username_textfield("Admin")
    login_obj.password_textfield("admin123")
    login_obj.login_btn()
    time.sleep(10)