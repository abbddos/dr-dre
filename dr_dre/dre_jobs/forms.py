from django import forms
from django.forms import ModelForm
from .models import Customer, Job

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email','phone_number','ride']


class JobCreationForm(ModelForm):
    class Meta:
        model = Job 
        fields = ['code', 'description', 'start_date','end_date','status','department','team','customer']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }