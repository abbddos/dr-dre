from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register_user'),
    path('GetAllUsers/', views.GetAllUsers, name = 'GetAllUsers'),
    path('GetUserByID/<uid>', views.GetUserByID, name = 'GetUserByID'),
    path('UpdateUser/<uid>', views.UpdateUser, name = 'UpdateUser')
]