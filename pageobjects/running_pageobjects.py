from selenium.webdriver.common.by import By


class RunningPageLocators:
    grid_items = "//a[@data-auto-id='glass-hockeycard-link']"
    close_popup = By.XPATH, "//button[@class='gl-modal__close']"
    header_text = "//h1[@data-auto-id='plp-header-bar-search-title']"
