from django.db import models
from dre_admin.models import Profile, Department, Team


class Customer(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 20)
    RegisterDate = models.DateField(blank = True)
    ride = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.name}'


class Job(models.Model):
    code = models.CharField(max_length = 8)
    description = models.CharField(max_length = 500)
    start_date = models.DateField()
    end_date = models.DateField(blank = True, null = True)
    status = models.CharField(max_length = 50, choices = [('Scheduled', 'Scheduled'),('In-Progress','In-Progress'),('On-Hold','On-Hold'),('Canceled','Canceled'),('Complete','Complete')], default = 'Scheduled')
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE, default = None)
    customer = models.ForeignKey('Customer', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.code}'


