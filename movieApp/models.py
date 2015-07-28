from django.db import models

# Create your models here.
#movie database
class Movie(models.Model):
    name = models.CharField(max_length=100)
    imdb_score = models.FloatField(null=True, blank=True)
    popularity = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.TextField(max_length=100)
	
    def __str__(self):
        return self.name

