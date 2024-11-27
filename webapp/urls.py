from django.urls import path
from webapp import views
urlpatterns=[
    path('home/',views.home,name='home'),
path('book_service/',views.book_service,name='book_service'),
path('residential_page/',views.residential_page,name='residential_page'),
path('save_enquiry/',views.save_enquiry,name='save_enquiry'),
path('application_plumber/',views.application_plumber,name='application_plumber')
]