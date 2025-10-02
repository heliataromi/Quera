from django.db import models

class WatchItem(models.Model):
    class TypeChoices(models.TextChoices):
        MOVIE = 'M', 'Movie'
        SERIES = 'S', 'Series'
    
    title = models.CharField()
    type = models.CharField(choices=TypeChoices.choices)
    poster = models.FileField(upload_to='posters/', blank=True, null=True, default='defaults/poster.jpg')
    url = models.URLField(blank=True, null=True)
    is_watched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
