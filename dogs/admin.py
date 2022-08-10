from django.contrib import admin
from .models import DogsModel

# Register your models here.
@admin.register(DogsModel)
class DogAdmin(admin.ModelAdmin):
    pass