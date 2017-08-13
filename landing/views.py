from django.shortcuts import render
from landing.backend import get_campaigns, get_train_predic, get_bus_predic

def index(request):

    bus_stops = ['1001454','1001442']
    train_stops = ['E02','A02']

    buses = []
    trains = []

    campaigns = get_campaigns()

    for stop in bus_stops:

        stop_info = get_bus_predic(stop)

        buses.append(stop_info)

    for station in train_stops:

        station_info = get_train_predic(station)

        trains.append(station_info)


    print(buses)
    print(trains)


    return render(request,'index.html', {
        'campaigns' : campaigns,
        'buses' : buses,
        'trains' : trains,
    })
