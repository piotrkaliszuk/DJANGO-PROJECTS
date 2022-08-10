from django.shortcuts import render
from authors.models import AuthorModel

# Create your views here.
def view_list(request):
    authors = AuthorModel.objects.all()
    return render(
        request=request,
        template_name='authors/view_list.html',
        context={
            'authors' : authors
        }
        
        )