import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    # Quit the driver after the test
    driver.quit()


def test_verify_title(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
