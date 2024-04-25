from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)
    capital = models.CharField(max_length=15)
    population = models.IntegerField()
    square = models.IntegerField()
    language = models.CharField(max_length=15)
    description = models.TextField()
