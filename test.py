import pytest
from selenium import webdriver
from base import Helper
from base import Base
import locators
import os

filepath = '/home/alman/pom_selenium/results_search.png'
filepath2 = '/home/alman/pom_selenium/results_relevancy.png'
filepath3 = '/home/alman/pom_selenium/results_symbols.png'


def screenshots():
    if os.path.exists(filepath):
        os.remove(filepath)
    elif os.path.exists(filepath2):
        os.remove(filepath2)
    elif os.path.exists(filepath3):
        os.remove(filepath3)
    else:
        print("No file was found")


def test_search(browser):
    search = Helper(browser)
    search.go_to_site()
    search.click_on_field()
    search.enter_word("Autocomplete ")
    element = search.dropdown5_check()
    assert "javascript" in element
    search.dropdown5()
    browser.save_screenshot(filename="results_search.png")


def test_relevancy(browser):
    relevancy = Helper(browser)
    relevancy.go_to_site()
    # relevancy.click_on_field()
    relevancy.enter_word("Autocomplete feature")
    relevancy.dropdown1_check()
    browser.save_screenshot(filename="results_relevancy.png")


def test_symbols(browser):
    symbols = Helper(browser)
    symbols.go_to_site()
    symbols.enter_word("!@$%^&*()-+={}[]:;”’<,>.?/")
    browser.save_screenshot(filename="results_symbols.png")
