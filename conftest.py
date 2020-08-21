import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.headless = False
    driver_path = "/home/alman/pom_selenium/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
