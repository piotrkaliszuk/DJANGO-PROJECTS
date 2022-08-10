from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=200,blank=False)
    rok_wydania = models.IntegerField(max_length=100,blank=True)
    opis = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title}, Rok {self.rok_wydania}, {self.opis}"


