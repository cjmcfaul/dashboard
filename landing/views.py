from django.shortcuts import render
from landing.backend import get_campaigns

def index(request):

    campaigns = get_campaigns()

    return render(request,'index.html', {
        'campaigns' : campaigns,
    })
