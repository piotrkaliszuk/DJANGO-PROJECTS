
from django.urls import path
from cats.views import view_list

urlpatterns = [
    path("", view_list)
]
