import os
import requests


def lambda_handler(request, context):
    if 'address' in request:
        return address_to_lat_lon(request)
    elif 'lat' in request and 'lon' in request:
        return lat_lon_to_address(request)
    else:
        raise Exception


def address_to_lat_lon(request):
    payload = {
        "address": request['address'],
        "key": os.environ['key']
    }
    json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?",params=payload).json()
    return json['results'][0]['geometry']['location']

def lat_lon_to_address(request):
    print(request)
    # payload = {
    #     "units": "imperial",
    #     "origins": "place_id:" + origin,
    #     "destinations": ["place_id:" + destination, "place_id:ChIJIyl5WALx7IARmBQ9sA-reRA"],
    # }
    # r = requests.get(url="https://maps.googleapis.com/maps/api/distancematrix/json", params=payload).json()
    # print(r)
    # return r['rows'][0]['elements'][0]['duration']['value'] / 60

