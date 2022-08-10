from django.shortcuts import render
from .models import DogsModel

# Create your views here.
def view_list(request):
    dogs = DogsModel.objects.all()
    return render(
        request=request,
        template_name='dogs/view_list.html',
        context={
            'dogs': dogs
        }
    )