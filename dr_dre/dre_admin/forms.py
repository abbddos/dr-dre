from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile, Department, Team

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'is_active']

class UserProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'department', 'team']


class DepartmentCreationForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dep_code', 'dep_name', 'dep_description']

class TeamCreationForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_code', 'team_name', 'team_dep', 'team_description']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']