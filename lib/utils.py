def convert_IATA_code_to_city_name(code: str) -> str:
    """
    Get airport city name from IATA 3-Letter Codes of Airports
    """
    airports_city = {
        "IST": 'Istanbul Airport',
        "DXB": 'Dubai Intl'
    }
    return airports_city[code]
