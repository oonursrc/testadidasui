from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageobjects.homepage_pageobjects import HopePageLocators
from pageobjects.running_pageobjects import RunningPageLocators
from pageobjects.shoe_pageobjects import ShoePageLocators
from tests.scripts.common import get_title


def is_title_correct(driver, title: str):
    """
    Verifies if webpage title is correct

    Parameters:
    driver: Selenium webdriver
    title: str type, title to be compared

    """
    current_title = get_title(driver)
    assert title in current_title, f"Web Page title {current_title} and " \
                                   f"expected title {title}  is not same"


def is_url_correct(driver, url: str):
    """
    Verifies if webpage url is correct

    Parameters:
    driver: Selenium webdriver
    url: str type, url to be compared

    """
    WebDriverWait(driver, 10).until(lambda x: url == driver.current_url)


def close_homepage_popups(driver):
    """
    Closes popup windows on homepage

    Parameters:
    driver: Selenium webdriver

    """
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HopePageLocators.close_popup)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HopePageLocators.accept_cookies)).click()


def search_products(driver, key):
    """
    Searches products based on given keyword

    Parameters:
    driver: Selenium webdriver
    key: str type, word to be used for product search

    """

    search = driver.find_element(By.XPATH, HopePageLocators.search_box)
    search.send_keys(key)
    search.send_keys(Keys.ENTER)


def click_on_first_product(driver):
    """
    Clicks to the first product

    Parameters:
    driver: Selenium webdriver

    """
    running_shoes_list = driver.find_elements(By.XPATH, RunningPageLocators.grid_items)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(running_shoes_list[0])).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RunningPageLocators.close_popup)).click()


def select_a_size(driver):
    """
    selects the first size of the product

    Parameters:
    driver: Selenium webdriver

    """
    shoe_size_list = driver.find_elements(By.XPATH, ShoePageLocators.shoe_sizes)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(shoe_size_list[0])).click()


def add_to_bag(driver):
    """
    adds selected product to the cart

    Parameters:
    driver: Selenium webdriver

    """
    driver.find_element(By.XPATH, ShoePageLocators.add_to_bag).click()
