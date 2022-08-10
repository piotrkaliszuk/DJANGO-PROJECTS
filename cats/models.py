
from django.db import models

# Create your models here.
class CatsModel(models.Model):
    imie = models.CharField(max_length=200,blank=False)
    rok_urodzenia = models.IntegerField(blank=True)
    rasa = models.CharField(max_length=200, blank=False)
    opis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.imie}, Rok {self.rok_urodzenia}, {self.rasa}, {self.opis},"


