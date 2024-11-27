from django.shortcuts import render,redirect, get_object_or_404
from adminapp.models import Details
from adminapp.models import Employeedb,Servicedb
from webapp.models import bookingdb,Enquiry,PlumberPartner
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def admin_index(request):
    return render(request,'admin_index.html')
def add_categories(request):
    return render(request,'add_categories.html')
def add_details(request):
    return render(request,'add_details.html')
def save_details(request):
    if request.method=="POST":
        a=request.POST.get('address')
        b = request.POST.get('phone')
        c = request.POST.get('email')

        obj=Details(Address=a,Phone=b,email=c)
        obj.save()


        return redirect(add_details)
def add_employee(request):
    return render(request,'create_employee.html')
def save_employee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        skills = request.POST.get('skills')
        location = request.POST.get('location')
        email = request.POST.get('email')

        # Create and save a new employee instance
        employee = Employeedb(
            name=name,
            age=age,
            gender=gender,
            skills=skills,
            location=location,
            email=email
        )
        employee.save()  # Save the instance to the database
        # Send email with the employee code
        subject = "Your Employee Code"
        message = f"Hello {employee.name},\n\nYour employee code is {employee.employee_code}.\n\nBest regards,\nPlumberz Union Afsal"
        recipient_list = [employee.email]

        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            # Optionally, add a success message here if using Django messages
        except Exception as e:
            # Optionally, handle the error or add an error message if email fails
            print(f"Error sending email: {e}")

        return redirect(add_employee)
def employee_list(request):
    employees = Employeedb.objects.all()  # Retrieve all employee records
    return render(request, 'employee_list.html', {'employees': employees})
def booking_requests(request):
    bookings = bookingdb.objects.all()  # Retrieve all booking entries
    return render(request, 'booking_request.html', {'bookings': bookings})
def add_service(request):
    return render(request,'add_service.html')
def save_service(request):
    if request.method == "POST":
        a = request.POST.get('service')
        b = request.POST.get('description')
        c = request.POST.get('price')


        # Create and save a new service instance
        service = Servicedb(
            service=a,
            description=b,
            price=c

        )
        service.save()  # Save the instance to the database

        return redirect(add_service)

def service_list(request):
    service = Servicedb.objects.all()  # Retrieve all employee records
    return render(request, 'service_list.html', {'service': service})

def booking_detail(request, job_code):
    # Retrieve the booking using the job_code
    try:
        booking = bookingdb.objects.get(job_code=job_code)  # This raises an exception if not found
        # Filter employers with matching location and/or skills
        employers = Employeedb.objects.filter(location=booking.location)

        # Calculate the match level for each employer
        matched_employers = []
        for employer in employers:
            match_count = 0
            # Check location match
            if employer.location == booking.location:
                match_count += 1
            # Check skills match
            booking_skills = set(booking.skills.split(','))
            employer_skills = set(employer.skills.split(','))
            skill_matches = len(booking_skills.intersection(employer_skills))
            match_count += skill_matches

            # Add employer and their match count to the list
            matched_employers.append({
                'employer': employer,
                'match_count': match_count,
                'skill_matches': skill_matches
            })

        # Sort employers by match level in descending order
        matched_employers.sort(key=lambda x: x['match_count'], reverse=True)
    except bookingdb.DoesNotExist:
        # If the booking does not exist, handle the error, e.g., return a 404 response
        return render(request, '404.html', status=404)  # Customize this as needed

    # If the booking is found, render the detail page
    return render(request, 'booking_detail.html', {'booking': booking,'matched_employers': matched_employers})


def view_enquiries(request):
    # Retrieve all enquiries from the database
    enquiries = Enquiry.objects.all()
    return render(request, 'view_enquiries.html', {'enquiries': enquiries})
def delete_enquiry(request, enquiry_id):
    enquiry = get_object_or_404(Enquiry, id=enquiry_id)
    enquiry.delete()
    messages.success(request, "Enquiry deleted successfully!")
    return redirect('view_enquiries')

def delete_booking(request, booking_id):
    # Get the booking object based on the ID
    booking = get_object_or_404(bookingdb, id=booking_id)

    if request.method == "POST":
        # Delete the booking object
        booking.delete()
        return redirect('booking_requests')  # Redirect to the booking requests page after deletion

    return HttpResponse(status=405)  # Method Not Allowed if not POST

def view_plumber_partners(request):
    # Fetch all PlumberPartner objects from the database
    partners = PlumberPartner.objects.all()

    # Render a page to display the details
    return render(request, 'view_application.html', {'partners': partners})



