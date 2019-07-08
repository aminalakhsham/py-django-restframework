from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  username = models.CharField(max_length=20, unique=True)
  email = models.EmailField()
  address = models.CharField(max_length=1000)
  phone_number = models.CharField(max_length=10)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ('email', 'first_name', 'last_name', 'address', 'phone_number')

  def __str__(self):
    return self.first_name + " " + self.last_name