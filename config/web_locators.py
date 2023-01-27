from selenium.webdriver.common.by import By


class Locators:
    ####### Home page #######
    tab_content = (By.ID, "TabContent")
    login_menu = (By.ID, "ACCOUNT")
    customer_login = (By.XPATH, "//a[@href='https://phptravels.net/login']")
    login_btn = (By.XPATH, "//span[text()='Login']/parent::button")
    username_field = (By.XPATH, "//input[@type='email']")
    password_field = (By.XPATH, "//input[@type='password']")

    ###### Flights booking page ######
    from_input = (By.ID, "autocomplete")
    destination_input = (By.ID, "autocomplete2")
    dashboard_btn = (By.XPATH, "//a[@href='https://phptravels.net/account/dashboard']")
    search_flight_btn = (By.XPATH, "//a[@href='https://phptravels.net/flights']")
    search_tab = (By.ID, "fadein")
    data_field = (By.ID, "departure")
    active_date = (By.XPATH, "//td[@class='day  active']")
    search_btn_id = "flights-search"
    search_results = (By.CLASS_NAME, "theme-search-results-item-mask-link")
    flights_list = (By.XPATH, "//ul[@class='catalog-panel']/li")
    price_child = (By.XPATH, "//button[@type='submit']")
    book_btn_child_xpath = "//button[@type='submit']"
    confirm_booking = (By.ID, "booking")
    booked_flights_list = (By.XPATH, "//div[@class='ItineraryTimeline']")
    departure = (By.XPATH, "//div[@class='ItineraryPartOverview-outbound']//span[@class='ItineraryPartOverviewField _name']")
    arrival = (By.XPATH, "//div[@class='ItineraryPartOverview-inbound']//span[@class='ItineraryPartOverviewField _name']")
    date = (By.XPATH, "//span[@class='ItineraryDate-date spTypo-medium']//time")
    airline = (By.XPATH, "//div[@class='ItineraryPartDetail _expanded']//span[@class='ItineraryPartDetail-item']")
    price = (By.XPATH, "//div[@class='card-body p-0']//strong")
    departure_time = (By.XPATH, "//div[@class='ItineraryPartOverview-outbound']//time")
    arrival_time = (By.XPATH, "//div[@class='ItineraryPartOverview-inbound']//time")

    @staticmethod
    def location_dropdown_script(text_val: str) -> str:
        return f"return $(\":contains('{text_val}'):last\").get(0);"

    @staticmethod
    def flight_time_xpath(airport):
        return f"//p[contains(text(), '{airport}')]/preceding-sibling::p"
