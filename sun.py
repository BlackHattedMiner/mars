# import required modules
import datetime
from suntime import Sun
from geopy.geocoders import Nominatim
import streamlit as st

# Nominatim API to get latitude and longitude
geolocator = Nominatim(user_agent="geoapiExercises")

# input place
place = "delhi"
location = geolocator.geocode(place)

# latitude and longitude fetch
latitude = location.latitude
longitude = location.longitude
sun = Sun(latitude, longitude)

# date in your machine's local time zone
time_zone = datetime.date(2021, 9,27)
sun_rise = sun.get_local_sunrise_time(time_zone)
sun_dusk = sun.get_local_sunset_time(time_zone)

# display
st.error("Sunrise Time:")
st.success(sun_rise.strftime('%H:%M'))
st.error("Sunset Time:")
st.success(sun_dusk.strftime('%H:%M'))
