from django.urls import path
from authors.views import view_list

urlpatterns = [
    path('', view_list)
]
