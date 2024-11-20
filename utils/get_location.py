from geopy.geocoders import Nominatim
import requests
import asyncio


def get_location_name(latitude, longitude):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Get location
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    # Extract address details
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    street = address.get('road', '')
    postcode = address.get('postcode', '')

    return {
        'city': city,
        'state': state,
        'country': country,
        'street': street,
        'postcode': postcode
    }


async def get_full_address(longitude, latitude):
    """This is open source map api to get full address, if it does not work return False"""
    await asyncio.sleep(1)
    url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
    response = requests.get(url)
    if response.status_code == 200:

        return response.json()['display_name']
    return False
