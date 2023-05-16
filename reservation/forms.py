from django import forms
from .models import OnlineBooking


class OnlineBookingForm(forms.ModelForm):
    class Meta:
        model = OnlineBooking
        fields = ['no_of_guest', 'date', 'time', 'occassion', 'special_request']
        exclude = ["user"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }