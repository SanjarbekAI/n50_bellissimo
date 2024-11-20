from geopy.geocoders import Nominatim


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
