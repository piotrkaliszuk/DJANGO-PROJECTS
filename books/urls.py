
from django.urls import path
from books.views import view_list

urlpatterns = [
    path("", view_list)
]
