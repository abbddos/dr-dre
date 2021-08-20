from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.Customers, name = 'customers'),
    path('GetAllCustomers/', views.GetAllCustomers, name = 'GetAllCustomers'),
    path('GetCustomerByID/<cid>', views.GetCustomerByID, name = 'GetCustomerByID'),
    path('UpdateCustomer/<cid>', views.UpdateCustomer, name = 'UpdateCustomer'),
    path('jobs/', views.Jobs, name = 'jobs'),
    path('UpdateJob/<jid>', views.UpdateJob, name = 'UpdateJob'),
    path('GetAllJobs/', views.GetAllJobs, name = 'GetAllJobs'),
    path('GetJobByID/<jid>', views.GetJobByID, name = 'GetJobByID'),
    path('GetJobsData/', views.GetJobsData, name = 'GetJobsData')
]