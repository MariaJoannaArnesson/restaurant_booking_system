from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OnlineBooking
from .forms import OnlineBookingForm
from datetime import date


def home(request):
    return render(request, 'home.html', {})


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

