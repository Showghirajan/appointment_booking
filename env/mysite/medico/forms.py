# forms.py
from django import forms
from .models import Appointment, Availability

class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(max_length=100, label="Patient Name")

    class Meta:
        model = Appointment
        fields = ['appointment_datetime']
        widgets = {
            'appointment_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day_of_week', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


        
