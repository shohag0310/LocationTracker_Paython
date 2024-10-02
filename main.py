import phonenumbers
import opencage
import folium
import webbrowser
import os
# import requests

from tempfile import NamedTemporaryFile
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


number="+8801912766655"
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))

key="e435fafa8803489eb97f2adab2e7f5ce"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]
print(lat, lng)


# # Google Maps Geocoding API key
# google_maps_api_key ="AIzaSyCNrEyPlrVYVj3T_61O4pcRPT_-e0OP2WE"

# # query = "Dhaka, Bangladesh"

# # Google Geocoding API URL
# url = f"https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={google_maps_api_key}"

# # Make the request
# response = requests.get(url)
# results = response.json()

# if results['status'] == 'OK':
#     # Get the first result
#     first_result = results['results'][0]
#     lat = first_result['geometry']['location']['lat']
#     lng = first_result['geometry']['location']['lng']
#     formatted_address = first_result['formatted_address']
    
#     print(f"Latitude: {lat}, Longitude: {lng}")
#     print(f"Formatted Address: {formatted_address}")
# else:
#     print("Geocoding request failed.")


my_map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(my_map)
# my_map.save("mylocation.html")

with NamedTemporaryFile(suffix=".html", delete=False) as temp_file:my_map.save(temp_file.name)
    
# webbrowser.open(f"file://{os.path.abspath(temp_file.name)}")
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open(f"file://{os.path.abspath(temp_file.name)}")

