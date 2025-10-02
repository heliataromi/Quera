from django.db import models

class GymMember(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    start_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
