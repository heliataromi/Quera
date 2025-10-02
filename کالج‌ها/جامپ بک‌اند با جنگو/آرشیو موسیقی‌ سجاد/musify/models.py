from django.db import models


class Singer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=200)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='songs')
    file = models.FileField(null=True, blank=True, upload_to='musics/')
    description = models.TextField(null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.singer}"
