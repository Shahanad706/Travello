from django.http import HttpResponse
from django.shortcuts import render
from .models import blog
from .models import place


# Create your views here.
def combined_view(request):
    places_list = place.objects.all()
    blogs_list = blog.objects.all()
    return render(request, "index.html", {'places': places_list, 'blogs': blogs_list})



