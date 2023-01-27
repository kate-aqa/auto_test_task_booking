import calendar
import re
from datetime import datetime as dt

from selenium.webdriver.common.by import By

from web_application.BasePage import BasePage
from config.web_locators import Locators
from lib.utils import convert_IATA_code_to_city_name


class FlightsBooking(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def search_flight(self, departure: str, arrival: str, date: str):
        self.open_flight_search()
        from_field = self.find_element(Locators.from_input)
        arrival_field = self.find_element(Locators.destination_input)
        from_field.send_keys(departure)
        departure_dropdown = self.driver.execute_script(Locators.location_dropdown_script(departure))
        departure_dropdown.click()
        arrival_field.send_keys(arrival)
        arrival_dropdown = self.driver.execute_script(Locators.location_dropdown_script(arrival))
        arrival_dropdown.click()
        date_field = self.find_element(Locators.data_field)
        date_field.clear()
        date_field.send_keys(date)
        self.find_element(Locators.active_date).click()
        self.driver.execute_script(f"document.getElementById('{Locators.search_btn_id}').click();")
        self.wait_for_page_load(Locators.search_results)

    def open_flight_search(self):
        self.find_element(Locators.search_flight_btn).click()
        self.wait_for_page_load(Locators.search_tab)

    def get_ordered_flights_list(self) -> list:
        """
        On search results page gets prices to ordered list
        """
        price_list = []
        data_items = self.find_elements(Locators.flights_list)
        for item in data_items:
            price = list(filter(lambda x: 'USD' in x, item.text.split("\n")))
            if price:
                price_val = re.findall(r"[-+]?\d*\.\d+|\d+", price[0])
                price_list.append(price_val[0])
        return price_list

    def get_cheapest_flight_info(self, items_to_check: dict) -> dict:
        """
        On search results page gets the cheapest flight and collect info according to items_to_check scope
        """
        flight_info_el = self.find_elements(Locators.flights_list)[0]
        departure_time = flight_info_el.find_element(by=By.XPATH, value=Locators.flight_time_xpath("DXB")).text
        arrival_time = flight_info_el.find_element(by=By.XPATH, value=Locators.flight_time_xpath("IST")).text
        data = flight_info_el.text.split("\n")
        items_to_check["flight no"] = data[1]
        items_to_check["price"] = re.findall(r"[-+]?\d*\.\d+|\d+", list(filter(lambda x: 'USD' in x, data))[0])[0]
        items_to_check["airline"] = data[0]
        items_to_check["departure time"] = dt.strftime(dt.strptime(departure_time, "%I:%M %p"), "%H:%M")
        items_to_check["arrival time"] = dt.strftime(dt.strptime(arrival_time, "%I:%M %p"), "%H:%M")
        return items_to_check

    def book_cheapest_flight(self):
        """
        On search results page book the cheapest flight
        """
        data_items = self.find_elements(Locators.flights_list)
        data_items[0].find_element(by=By.XPATH, value=Locators.book_btn_child_xpath).click()
        self.wait_for_page_load(Locators.confirm_booking)

    def get_flight_info(self) -> dict:
        """
        On booking confirmation page collect flight info
        """
        airline_info = []
        self.wait_text_element_loaded(Locators.date)
        date_to_convert = self.find_element(Locators.date).text.split(" ")
        airline_info_ = self.find_elements(Locators.airline)
        for item in airline_info_:
            airline_info.append(item.text)
        items_to_add = {
            "one way": len(self.find_elements(Locators.booked_flights_list)) == 1,
            "departure": convert_IATA_code_to_city_name(self.find_element(Locators.departure).text),
            "arrival": convert_IATA_code_to_city_name(self.find_element(Locators.arrival).text),
            "date": date_to_convert[0] + '-' + str(list(calendar.month_abbr).index(date_to_convert[2])) + '-' + date_to_convert[3],
            "flight no": airline_info[1].split(":")[1].strip(),
            "price": re.findall(r"[-+]?\d*\.\d+|\d+", self.find_element(Locators.price).text)[0],
            "airline": airline_info[0].split(":")[1].strip(),
            "departure time": self.find_element(Locators.departure_time).text[:5],
            "arrival time": self.find_element(Locators.arrival_time).text[:5]
        }
        return items_to_add
