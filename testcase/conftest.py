
from selenium import webdriver
import pytest
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

@pytest.fixture
def setup():
    driver = webdriver.Chrome(opts)
    print("Opening the Browser....")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    print("Closing the Browser....")
    driver.close()
    


