from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(config) -> webdriver:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            return driver

        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver

        raise Exception("Provide valid driver name")
