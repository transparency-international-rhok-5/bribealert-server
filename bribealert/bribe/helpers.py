from pygeocoder import Geocoder

from bribe.models import Country

def get_country_from_geo_location(lat, lon):
    results = Geocoder.reverse_geocode(lat, lon)
    country = Country.objects.get(name=str(results[-1]))
    
    return country