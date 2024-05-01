from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Country


def index(request):
    country = Country.objects.all()
    return render(request, 'infocountry/index.html', {'countries': country})


def show_descript(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    return render(request, 'infocountry/show_descriptions.html', {'countries': [country]})
