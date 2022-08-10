from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    secondary_name = models.CharField(max_length=200, blank=False)
    year_of_birdth = models.DateField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.secondary_name}'