from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view,name='signup'),
    path('profile/', views.profile_view,name='profile'),
    path('customers/', views.customer_list,name='customer_list'),
    path('customers/add/', views.add_customer,name='add_customer'),
    path('customers/edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
]