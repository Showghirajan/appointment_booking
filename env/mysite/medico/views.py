from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Patient, Appointment, Availability
from .forms import AppointmentForm, AvailabilityForm
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

def doctor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            doctor = Doctor.objects.get(email=email)
            if doctor.password == password:
                request.session['doctor_id'] = doctor.id
                return redirect('doctor_portal')
            else:
                messages.error(request, 'Invalid password. Please try again.')
        except Doctor.DoesNotExist:
            messages.error(request, 'No account found with this email.')
    return render(request, 'doctor_login.html')


def doctor_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        specialization = request.POST['specialization']
        password = request.POST['password']
        
        if Doctor.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please log in.')
            return redirect('doctor_login')
        
        # Create a new doctor
        new_doctor = Doctor.objects.create(name=name, email=email, specialization=specialization, password=password)
        new_doctor.save()
        
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('doctor_login')
    
    return render(request, 'doctor_signup.html')


def patient_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            patient = Patient.objects.get(email=email)
            if patient.password == password:
                request.session['patient_id'] = patient.id
                return redirect('patient_portal')
            else:
                messages.error(request, 'Invalid password. Please try again.')
        except Patient.DoesNotExist:
            messages.error(request, 'No account found with this email.')
    return render(request, 'patient_login.html')


def patient_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        
        if Patient.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists. Please log in.')
            return redirect('patient_login')
        
        # Create a new patient
        new_patient = Patient.objects.create(name=name, email=email, password=password)
        new_patient.save()
        
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('patient_login')
    
    return render(request, 'patient_signup.html')



def patient_portal(request):
    # Fetch all doctors with their related availability using select_related uses "ORM"
    doctors = Doctor.objects.prefetch_related('availability_set').all()
    return render(request, 'patient_portal.html', {'doctors': doctors})


def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            patient_id = request.session.get('patient_id')
            if not patient_id:
                messages.error(request, 'Please log in to book an appointment.')
                return redirect('patient_login')
            try:
                patient = Patient.objects.get(id=patient_id)
            except Patient.DoesNotExist:
                messages.error(request, 'Patient not found.')
                return redirect('patient_login')
            appointment.patient = patient
            appointment.doctor = doctor
            appointment.status = 'PENDING'
            appointment.save()
            return redirect('patient_status')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form, 'doctor': doctor})

def doctor_portal(request):
    doctor_id = request.session.get('doctor_id')
    if not doctor_id:
        return redirect('doctor_login')
    
    doctor = Doctor.objects.get(id=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor, status='PENDING')
    availability = Availability.objects.filter(doctor=doctor)

    # Handle availability form submission
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            new_availability = form.save(commit=False)
            new_availability.doctor = doctor  # Assign the current doctor
            new_availability.save()
            return redirect('doctor_portal')
    else:
        form = AvailabilityForm()

    return render(request, 'doctor_portal.html', {
        'appointments': appointments,
        'availability': availability,
        'form': form
    })

def update_appointment_status(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        status = request.POST['status']
        appointment.status = status
        appointment.save()
        return redirect('doctor_portal')
    return render(request, 'update_appointment_status.html', {'appointment': appointment})

def patient_appointments(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient_login')
    patient = Patient.objects.get(id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient_appointments.html', {'appointments': appointments})

def patient_status(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient_login')
    patient = Patient.objects.get(id=patient_id)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'patient_status.html', {'appointments': appointments})



def appointment_decision(request, appointment_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        appointment = get_object_or_404(Appointment, id=appointment_id)

        if action == 'accept':
            appointment.status = 'ACCEPTED'
        elif action == 'reject':
            appointment.status = 'REJECTED'

        appointment.save()
        
    return redirect('doctor_portal')


from django.shortcuts import redirect





