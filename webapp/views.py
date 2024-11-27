from django.shortcuts import render,redirect,HttpResponse
from adminapp.models import Details,Employeedb,Servicedb
from webapp.models import bookingdb
from datetime import datetime
from django.contrib import messages
from .models import Enquiry,PlumberPartner

# Create your views here.
def home(request):
    details = Details.objects.first()
    service=Servicedb.objects.all()
    employee=Employeedb.objects.all()
    return render(request,'home.html',{'details':details,'service':service,'employee':employee})
def book_service(request):
    if request.method == 'POST':
        # Get data from the form fields
        user_name = request.POST.get('name')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        date = request.POST.get('date')
        request_text = request.POST.get('request')
        location=request.POST.get('location')
        try:
            date = datetime.strptime(date, '%m/%d/%Y').date()
        except ValueError:
            return HttpResponse("Invalid date format. Please use MM/DD/YYYY.")

        # Save data to the model
        booking = bookingdb(
            user_name=user_name,
            phone=phone,
            service=service,
            location=location,
            skills=request_text,
            date=date
        )
        booking.save()

        return redirect(home)

def residential_page(request):
    return render(request,'residential_page.html')

def save_enquiry(request):
    if request.method == 'POST':
        # Get form data
        category = request.POST.get('category')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        budget = request.POST.get('budget')
        bathrooms = request.POST.get('bathrooms')
        area = request.POST.get('area')
        location = request.POST.get('location')
        date = request.POST.get('date')
        request_notes = request.POST.get('request', '')

        # Save the data to the model
        enquiry = Enquiry(
            category=category,
            name=name,
            phone=phone,
            budget=budget,
            bathrooms=bathrooms,
            area=area,
            location=location,
            date=datetime.strptime(date, '%Y-%m-%d').date(),
            request=request_notes,
        )
        enquiry.save()

        # Add a success message
        messages.success(request, "Successfully sent request for booking!")
        return redirect('residential_page')  # Replace with your URL name for this page

def application_plumber(request):
    return render(request,'application_page.html')

def application_plumber(request):
    if request.method == "POST":
        # Get data from the form
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        skills = request.POST.get('skills')
        location = request.POST.get('location')
        employee_code = request.POST.get('employee_code')
        email = request.POST.get('email')

        # Save the data to the database
        plumber_partner = PlumberPartner(
            name=name,
            age=age,
            gender=gender,
            skills=skills,
            location=location,
            employee_code=employee_code,
            email=email
        )
        plumber_partner.save()

        # Redirect to a success page or back to the form page
        return redirect('home')

