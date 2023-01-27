from web_application.HomePage import HomePage
from web_application.FlightsBookingPage import FlightsBooking


def test_check_booking_should_be_successful(web_browser):
    """
    Test verifies that the booking is successful and that the flight details (items_to_check) are displayed correctly
    on the booking confirmation page
    """

    items_to_check = {
        "one way": True,
        "departure": "Dubai Intl",
        "arrival": "Istanbul Airport",
        "date": "05-2-2023",
        "flight no": None,
        "price": None,
        "airline": None,
        "departure time": None,
        "arrival time": None
    }

    page = FlightsBooking(web_browser)
    HomePage(web_browser).login()
    page.search_flight(departure=items_to_check["departure"], arrival=items_to_check["arrival"], date=items_to_check["date"])

    # check results are sorted by price
    price_list = page.get_ordered_flights_list()
    assert price_list == sorted(price_list)

    to_book = page.get_cheapest_flight_info(items_to_check)
    page.book_cheapest_flight()
    booking_result = FlightsBooking(web_browser).get_flight_info()
    assert to_book == booking_result
