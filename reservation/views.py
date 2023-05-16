from django.shortcuts import render, redirect, HttpResponse, get_list_or_404, \
    get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date
from django.contrib import messages


def home(request):
    return render(request, 'home.html', {})

def reservation(request):
    return render(request, 'reservation.html')    


@login_required
def online_booking(request):

    if request.method == 'POST':
        form = OnlineBookingForm(request.POST)

        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(
                request, 'Reservation request submitted succesfully.'
                )
        else:
            messages.error(request, 'The table is already booked.')
            reservation = form.instance.date

    form = OnlineBookingForm()
    context = {
        'form': form,
    }
    return render(request, 'online_booking.html', context)


@login_required
def mybookings(request):
    try:
        online_bookings = get_list_or_404(OnlineBooking, user=request.user)
    except Exception:
        online_bookings = None

    form = OnlineBookingForm()
    context = {
        'online_bookings': online_bookings,
    }
    return render(request, 'mybookings.html', context)