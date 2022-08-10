from django.shortcuts import render
from .models import BookModel
# Create your views here.
def view_list(request):
    books = BookModel.objects.all()
    return render(
        request=request,
        template_name="books/view_list.html",
        context={
            "books": books
        }
    )
