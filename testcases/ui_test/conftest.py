
import pytest
from playwright.sync_api import sync_playwright
from common.handle_config import conf


@pytest.fixture(scope='function')
def login_fixture():
    with sync_playwright() as p:
        url = conf.get('test3-rest', 'url')
        browser = p.chromium.launch(headless=False, args=['--start-maximized'])
        content = browser.new_context(no_viewport=True)
        page = content.new_page()
        page.goto(url)
        yield page
