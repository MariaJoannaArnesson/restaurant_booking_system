from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reservation', views.reservation, name='reservation'),
    path('online_booking', views.online_booking, name='online_booking'),
    path('mybookings', views.mybookings, name='mybookings'),
]