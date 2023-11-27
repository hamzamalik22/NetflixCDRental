from django.db import models
from django.utils import timezone

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    Released_year = models.IntegerField()
    Number_in_Stock = models.IntegerField()
    rental_rate = models.FloatField()
    category = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre , on_delete=models.CASCADE)


    def __str__(self):
        return self.name