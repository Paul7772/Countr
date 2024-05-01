from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    capital = models.CharField(max_length=15)
    population = models.IntegerField()
    square = models.IntegerField()
    language = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['name'])
        ]