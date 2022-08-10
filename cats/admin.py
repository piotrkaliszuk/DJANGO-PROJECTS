from django.contrib import admin
from .models import CatsModel


# Register your models here.


@admin.register(CatsModel)
class CatsAdmin(admin.ModelAdmin):
    pass
