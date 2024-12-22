from django.contrib import admin

# Register your models here.
from .models import Doctor, Patient, Availability, Appointment

# Register your models here
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Availability)
admin.site.register(Appointment)