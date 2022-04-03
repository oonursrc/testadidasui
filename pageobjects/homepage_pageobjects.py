from selenium.webdriver.common.by import By


class HopePageLocators:
    close_popup = By.XPATH, "//button[@class='gl-modal__close']"
    accept_cookies = By.XPATH, "//*[contains(@class,'text-wrap___3Cntx')]"
    search_box = "//input[@name='q']"
