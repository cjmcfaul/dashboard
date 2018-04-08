from django.shortcuts import render
from landing.backend import get_distance, find_train_stations, search_place, find_bus_stops, get_campaigns, get_train_predic, get_lights, get_bus_predic, get_crypto
from dashboard.secret_settings import *
from django.utils import timezone

try:
    dash_place = search_place('1428+Montello+Ave+NE+Washington,DC')

    dash_place_lat = dash_place[0]
    dash_place_lng = dash_place[1]
    dash_place_lat_lng = str(dash_place_lat) + "+" + str(dash_place_lng)
    stops_near = find_bus_stops(dash_place_lat,dash_place_lng,2000)

except:

    stops_near = []

my_crypto_list = [
    ['tron',3089.994],
    ['bitcoin',.00516199],
    ['ethereum',.09369720],
    ['ripple',26.973],
    ['nano',1.86813],
    ]

def index(request):

    house_lights = get_lights()

    now = timezone.now()

    crypto_list = []
    crypto_total = 0

    for coin in my_crypto_list:

        crypto_item = get_crypto(coin[0],coin[1])
        crypto_total = crypto_total + crypto_item['value']

        crypto_list.append(crypto_item)

    #stations_near = find_train_stations(dash_place_lat,dash_place_lng,2000)

    bus_stops = []
    #train_stations = ['E02']

    b = 0
    for item in stops_near:
        stop_lat = stops_near['Stops'][b]['Lat']
        stop_lng = stops_near['Stops'][b]['Lon']
        stop_id = stops_near['Stops'][b]['StopID']
        bus_stops.append([str(stop_lat), str(stop_lng), stop_id])
        b+=1

    t = 0
    '''
    for item in stations_near:
        train_stations.append(stations_near['Entrances'][t]['StationCode1'])
        try:
            train_stations.append(stations_near['Entrances'][t]['StationCode2'])
        except:
            print('No 2nd station code')
        t+=1
    '''
    buses = []
    #trains = []

    for stop in bus_stops:
        stop_lat = stop[0]
        stop_lng = stop[1]
        stop_lat_lng = stop_lat + "+" + stop_lng
        distance = None #get_distance(dash_place_lat_lng, stop_lat_lng)
        stop_predic = get_bus_predic(stop[2])
        print(distance)
        stop_info = [stop, stop_predic, distance]
        buses.append(stop_info)
    '''
    for station in train_stations:

        station_info = get_train_predic(station)
        trains.append(station_info)
    '''
    return render(request,'index.html', {
        'buses' : buses,
        'house_lights' : house_lights,
        'now' : now,
        'crypto_list': crypto_list,
        'crypto_total': crypto_total,
    })
