from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('reservation', views.reservation, name='reservation'),
    path('menu', views.menu, name='menu'),
    path('online_booking', views.online_booking, name='online_booking'),
    path('mybookings', views.mybookings, name='mybookings'),
    path(
        'edit_booking/<online_booking_id>',
        views.edit_booking, name='edit_booking'
    ),
]