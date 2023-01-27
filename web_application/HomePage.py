from web_application.BasePage import BasePage
from config.web_locators import Locators
from config.config import Config as cf


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://phptravels.net/"

    def login(self):
        self.driver.get(self.url)
        self.wait_for_page_load(Locators.tab_content)
        self.find_element(Locators.login_menu).click()
        self.find_element(Locators.customer_login).click()
        username_field = self.find_element(Locators.username_field)
        password_field = self.find_element(Locators.password_field)
        username_field.send_keys(cf.login)
        password_field.send_keys(cf.password)
        self.find_element(Locators.login_btn).click()
        self.wait_for_page_load(Locators.dashboard_btn)

