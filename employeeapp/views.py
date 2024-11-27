from django.shortcuts import render,redirect
from employeeapp.models import signindb
from adminapp.models import Employeedb
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.models import bookingdb,Enquiry
from datetime import datetime, timedelta
# Create your views here.

def index(request):
    username = request.session.get('username')
    customer = signindb.objects.filter(employee_code=username).first()  # Use `first()` for specific user instead of ordering by id
    if not customer:
        return redirect('login_employee')  # Redirect if the customer doesn't exist

    booking_data = None
    enquiry_data = None

    # Check if subscription has expired
    if customer.subscription_end_date and customer.subscription_end_date < datetime.today().date():
        # Subscription expired, clear it
        customer.subscription_type = None
        customer.subscription_end_date = None
        customer.save()

    # Handle subscription POST request
    if request.method == "POST":
        subscription_type = request.POST.get('subscription_type')
        if subscription_type == "Bronze":
            amount = 5
        elif subscription_type == "Platinum":
            amount = 10
        else:
            amount = 0  # Default fallback

        amount = int(amount * 100)  # Convert to paise (for Razorpay)

        # Create Razorpay client and initiate payment
        client = razorpay.Client(auth=('rzp_test_f9tvF898lXtAoP', '33gATP6Hen3bdhgYhRI29SGN'))
        payment = client.order.create({'amount': amount, 'currency': 'INR'})

        # Update subscription details
        customer.subscription_type = subscription_type
        customer.subscription_end_date = datetime.today().date() + timedelta(days=30)  # Set 30 days from now
        customer.save()

        context = {
            'customer': customer,
            'payy_str': str(amount),
            'payment': payment,
            'subscription_type': subscription_type,
        }
        return render(request, 'index.html', context)

    # Fetch data based on active subscription
    if customer.subscription_type:
        if customer.subscription_type == "Bronze":
            booking_data = bookingdb.objects.all()  # Fetch all booking data
        elif customer.subscription_type == "Platinum":
            booking_data = bookingdb.objects.all()  # Fetch booking data
            enquiry_data = Enquiry.objects.all()  # Fetch enquiry data

    # Render the page with customer data and subscription status
    return render(request, 'index.html', {
        'customer': customer,
        'username': username,
        'booking_data': booking_data,
        'enquiry_data': enquiry_data
    })


def login_employee(request):
    return render(request,'login_page.html')
def sign_employee(request):
    return render(request,'sign_in.html')

def save_user(request):
    if request.method == "POST":
        employee_code = request.POST.get('employee_code')
        password = request.POST.get('p1')

        # Check if the entered employee_code exists in the Employee model (admin app)
        if not Employeedb.objects.filter(employee_code=employee_code).exists():
            return redirect('sign_employee')  # Redirect to sign up page if code doesn't exist

        # Check if the employee_code is already used in the signindb table
        if signindb.objects.filter(employee_code=employee_code).exists():
            return redirect('sign_employee')  # Redirect to sign-up page if employee code is already used

        # Save the employee details (signindb model)
        obj = signindb(employee_code=employee_code, password=password)
        obj.save()
        return redirect('login_employee')  # Redirect to login page after successful
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('employee_code')
        pwd=request.POST.get('password')
        if signindb.objects.filter(employee_code=un,password=pwd):
            request.session['username']=un
            request.session['password']=pwd
            return redirect(index)
        else:
            return redirect(login_employee)
def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_employee)

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        # Process the payment success response from Razorpay
        # Update user subscription status here
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})







