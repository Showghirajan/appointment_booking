# doctor_patient_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_signup/', views.patient_signup, name='patient_signup'),
   
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_signup/', views.doctor_signup, name='doctor_signup'),

    path('patient/portal/', views.patient_portal, name='patient_portal'),
    path('book/appointment/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
    path('doctor/portal/', views.doctor_portal, name='doctor_portal'),
    path('patient/appointments/', views.patient_appointments, name='patient_appointments'),

    path('patient/status/', views.patient_status, name='patient_status'),
    path('appointment/<int:appointment_id>/decision/', views.appointment_decision, name='appointment_decision'),
    path('update/appointment/status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
]