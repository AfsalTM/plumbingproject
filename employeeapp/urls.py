from django.urls import path
from employeeapp import views
urlpatterns=[
path('login_employee/',views.login_employee,name='login_employee'),
path('sign_employee/',views.sign_employee,name='sign_employee'),
path('index/',views.index,name='index'),
path('save_user/',views.save_user,name='save_user'),
path('user_login/',views.user_login,name='user_login'),
path('user_logout/',views.user_logout,name='user_logout'),
    path('payment_success/', views.payment_success, name='payment_success')
]