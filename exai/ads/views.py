from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'ads/index.html'
    return render(request, template)


def ads_detail(request, pk):
    return HttpResponse(f'Автомобиль номер {pk}')
