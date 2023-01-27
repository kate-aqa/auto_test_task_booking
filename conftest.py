import pytest
from selenium import webdriver
import selenium.webdriver.chrome.options as chrome_options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import get_download_dir, Config


@pytest.fixture
def web_browser():
    options = chrome_options.Options()
    prefs = {"profile.default_content_setting_values.automatic_downloads": 2,
             "download.default_directory": get_download_dir(),
             "download.prompt_for_download": False,
             "safebrowsing.enabled": True,
             "directory_upgrade": True}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.headless = Config.headless
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()
