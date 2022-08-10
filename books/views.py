from django.shortcuts import render

# Create your views here.
def view_list(request):
    return render(
        request=request,
        template_name="books/view_list.html"
    )
