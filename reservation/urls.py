from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('online_booking', views.online_booking, name='online_booking'),
]