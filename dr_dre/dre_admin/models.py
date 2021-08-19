from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length = 50, choices = [('Admin','Admin'),('Department Head','Department Head'),('Team Leader','Team Leader'),('User','User')], default = 'User')
    department = models.ForeignKey('Department', on_delete = models.CASCADE, default = 1)
    team = models.ForeignKey('Team', on_delete = models.CASCADE, default = 1)
    def __str__(self):
        return f'{self.user.username} Profile'



class Department(models.Model):
    dep_code = models.CharField(max_length = 20, unique = False, default = 'All')
    dep_name = models.CharField(max_length = 30,  default = 'All')
    dep_description = models.CharField(max_length = 400, null = True)

    def __str__(self):
        return f'{self.dep_name}'


class Team(models.Model):
    team_code = models.CharField(max_length = 30, unique = True, default = 'All')
    team_name = models.CharField(max_length = 40,  default = 'All')
    team_dep = models.ForeignKey('Department', on_delete = models.CASCADE, default = 1)
    team_description = models.CharField(max_length = 400, null = True)

    def __str__(self):
        return f'{self.team_name}'
