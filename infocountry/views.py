from django.shortcuts import render
from .models import Country

def index(request):
    country = Country.objects.all()
    return render(request, 'infocountry/index.html', {'country': country})
