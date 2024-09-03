from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	national_code = models.CharField(max_length=10, unique=True)
	height = models.IntegerField()
	father_name = models.CharField(max_length=50)
