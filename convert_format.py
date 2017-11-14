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
    payload = {
        "address": str(request['lat']) + ',' + str(request['lon']),
        "key": os.environ['key']
    }
    json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?",params=payload).json()
    return json['results'][0]['formatted_address']

