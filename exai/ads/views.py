from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


# Главная страница
def index(request):
    cars = Car.objects.order_by('-mileage')
    context = {
        'cars': cars
    }
    template = 'ads/index.html'
    return render(request, template, context)


def ads_detail(request, pk):
    return HttpResponse(f'Автомобиль номер {pk}')
