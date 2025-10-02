from django import forms
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.coach})"


class Enrollment(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course', 'national_id')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course.name}"
