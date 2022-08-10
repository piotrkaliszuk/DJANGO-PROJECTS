from django.urls import path
from dogs.views import view_list

urlpatterns = [
    path('', view_list)
]
