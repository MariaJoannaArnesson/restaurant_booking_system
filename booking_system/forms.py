from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['no_of_guest', 'date', 'time']
        exclude = ["user"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }