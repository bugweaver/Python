from django.shortcuts import render
from .models import Cities


def index(request):
    cities = Cities.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})
