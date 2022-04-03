

def find_element(driver, *locator):
    return driver.find_element(*locator)


def open_url(driver, url):
    driver.get(url)


def get_title(driver):
    return driver.title


def get_url(driver):
    return driver.current_url


def close_page(driver):
    driver.quit()
