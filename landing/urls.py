from django.conf.urls import url
from landing import views

urlpatterns = [
    url(r'^home/$', views.index, name='home'),
]
