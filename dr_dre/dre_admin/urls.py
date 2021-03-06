from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register_user'),
    path('departments/', views.Departments, name = 'departments'),
    path('GetAllUsers/', views.GetAllUsers, name = 'GetAllUsers'),
    path('GetUserByID/<uid>/', views.GetUserByID, name = 'GetUserByID'),
    path('UpdateUser/<uid>', views.UpdateUser, name = 'UpdateUser'),
    path('GetAllDepartments/', views.GetAllDepartments, name = 'GetAllDepartments'),
    path('GetDepartmentByID/<did>/', views.GetDepartmentByID, name = 'GetDepartmentByID'),
    path('UpdateDepartment/<did>', views.UpdateDepartment, name = 'UpdateDepartment'),
    path('teams', views.Teams, name = 'teams'),
    path('GetAllTeams', views.GetAllTeams, name = 'GetAllTeams'),
    path('GetTeamByID/<tid>', views.GetTeamByID, name = 'GetTeamByID'),
    path('UpdateTeam/<tid>', views.UpdateTeam, name = 'UpdateTeam')
]