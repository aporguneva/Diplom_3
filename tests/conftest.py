import pytest
from selenium import webdriver
from data.urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()

    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get(Urls.BASE_URL)

    yield driver

    driver.quit()