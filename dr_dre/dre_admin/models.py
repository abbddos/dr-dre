from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length = 50, choices = [('Admin','Admin'),('Department Head','Department Head'),('Team Leader','Team Leader'),('User','User')], default = 'User')

    def __str__(self):
        return f'{self.user.username} Profile'


