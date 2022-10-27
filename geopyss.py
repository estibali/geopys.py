
from geopy.geocoders import Nominatim
geolocate= Nominatim(user_agent="geopyss.py")
ubi=geolocate.reverse("19.2718268,-98.825261")
print(ubi.address)
print(ubi.latitude,ubi.longitude)

"""


from geopy.geocoders import GoogleV3
punto='19.2718268,-98.825261'
geolocate=GoogleV3(api_key="geopyss.py")
direccion=geolocate.bounds(punto)
print(direccion[0])
"""