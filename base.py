from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.google.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Cannot find an element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                     message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)


class Helper(Base):
    def click_on_field(self):
        return self.find_element(locators.SEARCH_FIELD, time=2).click()

    def enter_word(self, word):
        search_box = self.find_element(locators.SEARCH_FIELD)
        search_box.click()
        search_box.send_keys(word)
        return search_box

    def dropdown5(self):
        autofill = self.find_element(locators.DROPDOWN5, time=2)
        return autofill.click()

    def dropdown5_check(self):
        indicator = self.find_element(locators.DROPDOWN5_TEXT, time=2)
        print(indicator)
        return indicator.text

    def dropdown1_check(self):
        indicator = self.find_element(locators.DROPDOWN1, time=2)
        return indicator.click()



