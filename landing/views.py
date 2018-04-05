from django.shortcuts import render
from landing.backend import get_distance, find_train_stations, search_place, find_bus_stops, get_campaigns, get_train_predic, get_bus_predic

try:
    dash_place = search_place('1428+Montello+Ave+NE+Washington,DC')

    dash_place_lat = dash_place[0]
    dash_place_lng = dash_place[1]
    dash_place_lat_lng = str(dash_place_lat) + "+" + str(dash_place_lng)
    stops_near = find_bus_stops(dash_place_lat,dash_place_lng,2000)

except:

    stops_near = []

def index(request):

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
        distance = get_distance(dash_place_lat_lng, stop_lat_lng)
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
    })
