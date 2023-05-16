import googlemaps
import os

gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_DIRECTIONS_API_KEY'))

def get_directions_to_city_center_in_minutes(address):
    directions_result = gmaps.directions(address, "метро Хрещатик, Київ", mode="walking")
    print(directions_result, 'direction API response')
    return directions_result[0]['legs'][0]['duration']['value'] / 60
