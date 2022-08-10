from django.db import models

# Create your models here.
class DogsModel(models.Model):
    name = models.CharField(max_length=200, blank=False)
    breed = models.CharField(max_length=200, blank=False)
    year_of_birdth = models.DateField(blank=False)

    def __str__(self) -> str:
        return f'{self.name} {self.breed} {self.year_of_birdth}'