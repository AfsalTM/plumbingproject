from django.urls import path
from adminapp import views
urlpatterns=[
path('admin_index/',views.admin_index,name='admin_index'),
path('add_categories/',views.add_categories,name='add_categories'),
path('add_details/',views.add_details,name='add_details'),
path('save_details/',views.save_details,name='save_details'),
path('add_employee/',views.add_employee,name='add_employee'),
path('save_employee/',views.save_employee,name='save_employee'),
path('employee_list/',views.employee_list,name='employee_list'),
path('booking_requests/',views.booking_requests,name='booking_requests'),
path('add_service/',views.add_service,name='add_service'),
path('save_service/',views.save_service,name='save_service'),
path('service_list/',views.service_list,name='service_list'),
path('booking/<str:job_code>/',views.booking_detail, name='booking_detail'),
path('view_enquiries/', views.view_enquiries, name='view_enquiries'),
path('delete_enquiry/<int:enquiry_id>/', views.delete_enquiry, name='delete_enquiry'),
path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
path('view_plumber_partners/', views.view_plumber_partners, name='view_plumber_partners')

]