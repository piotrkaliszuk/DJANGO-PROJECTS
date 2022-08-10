
from django.shortcuts import render
from django.template import loader
from .models import CatsModel
# Create your views here.
def view_list(request):
    cats = CatsModel.objects.all()
    return render(
        request=request,
        template_name="cats/view_list.html",
        context={
            "cats": cats
        }
    )
