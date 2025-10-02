from django.db import models


class Course(models.Model):
    poster_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.title
