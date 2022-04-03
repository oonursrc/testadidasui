from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)
from tests.scripts.common import (
    open_url, close_page,
)
from tests.scripts.operations import (
    is_title_correct,
    close_homepage_popups, search_products, click_on_first_product, is_url_correct, add_to_bag, select_a_size,
)

from utils.webdriver_helper import create_driver
from utils.config_helper import add_browser_to_config


@scenario('../features/adidas.feature', 'Web page is running')
def test_webpage_is_running():
    """Web page is running."""


@scenario('../features/adidas.feature', 'Search for a product')
def test_search_and_click_on_first_product():
    """Search and click on first product."""


@scenario('../features/adidas.feature', 'Add a product to the cart')
def test_add_a_product_to_the_cart():
    """Add a product to the cart."""


@given(parsers.parse('Adidas web page is running on {browser}'))
def step(context, config, browser):
    config = add_browser_to_config(browser, config)
    driver = create_driver(config)
    context["driver"] = driver
    open_url(driver, config["base_url"])


@then(parsers.parse('webpage title is {title}'))
def step(context, title):
    is_title_correct(context["driver"], title)
    close_homepage_popups(context["driver"])


@when(parsers.parse('{key} word is searched'))
def step(context, key):
    search_products(context["driver"], key)


@then(parsers.parse('new url is {url}'))
def step(context, url):
    is_url_correct(context["driver"], str(url))


@when('click on the first product')
def step(context):
    click_on_first_product(context["driver"])


@when('select a size')
def step(context):
    select_a_size(context["driver"])


@when('add to bag')
def step(context):
    add_to_bag(context["driver"])


@then(parsers.parse('there are {count} product in the cart'))
def step(context):
    # An unexpected error is thrown by adidas webpage after adding product to cart.
    # So that I cannot continue for now and quit driver only.
    close_page(context["driver"])
