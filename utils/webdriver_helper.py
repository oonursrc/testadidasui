from utils.DriverFactory import DriverFactory


def create_driver(config):
    driver = DriverFactory.get_driver(config)
    driver.implicitly_wait(config["timeout"])
    return driver
