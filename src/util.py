from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
import folium

class Util:
    def get_location(address):
        search = "{} - Belo Horizonte".format(address)
        locator = Nominatim(user_agent="myGeocoder")
        return locator.geocode(search)

    def get_location2(address):    
        locator = Nominatim(user_agent="myGeocoder")
        return locator.geocode(address)

    def get_map(address, zoom=15):
        location = Util.get_location(address)
        if(location):
            m = folium.Map(location=[location.latitude, location.longitude], zoom_start=zoom)
            folium.Marker([location.latitude, location.longitude]).add_to(m)
            folium_static(m) 
    
    def format_month(month):    
        if(month > 1):
            return 'meses'
        return 'mês'
        