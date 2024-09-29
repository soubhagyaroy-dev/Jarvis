import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

number = input("Enter your number : ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
sim_details = carrier.name_for_number(phone,"en")
register = geocoder.description_for_number(phone,"en")
location = geocoder.description_for_number(phone,"en")
key = '53bac2b6ec4e4a9aa1b49535f34affa6'
geocoder = OpenCageGeocode(key)
que = (location)
result = geocoder.geocode(que)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

# Map method of folium return Map object

# Here we pass coordinates of user
# and starting Zoom level = 12
myMap = folium.Map(location = [lat, lng],zoom_start = 12 )
folium.Marker([lat,lng],popup=location).add_to(myMap)

# save method of Map object will create a map
myMap.save("myMap.html")

print(number)
print(phone)
print(time)
print(sim_details)
print(register)
print(location)
print(result)
print(lat,lng)