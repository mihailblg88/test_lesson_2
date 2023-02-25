import pytest
from selene import be, have
from selene import browser


@pytest.fixture()
def browser_size():
    browser.config.window_height = 720
    browser.config.window_width = 1280


@pytest.fixture()
def browser_open(browser_size):
    browser.open('https://google.com/')


def test_web_search_positiv(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka\selene').press_enter()


def test_web_search_negative(browser_open):
    browser.element('[name="q"]').should(be.blank).type('775855IIIIIpp!!!').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу 775855IIIIIpp!!! ничего не найдено.'))
