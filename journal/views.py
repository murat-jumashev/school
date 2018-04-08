import datetime
from django.shortcuts import render

from .models import Transport

class Home:
    def __init__(self, qty):
        self.__stories_num = qty
        self.name = 'Үйүм'

    def get_stories(self):
        basement = 1
        return self.__stories_num + basement


def index(request):
    my_house = Home(3)
    dictionary = {
        'Kyrgyzstan': 'Bishkek',
        'Kazakhstan': 'Astana'
    }
    list_of_cars = Transport.objects.filter(year_of_production__gte=2017)
    one_car = Transport.objects.get(pk=1)
    null_value = True
    NUMBER_OF_DAYS = 2
    record_from_db = None
    today = datetime.datetime.today()
    context = {
        'aidar': 'Aidar Abdyrahmanov',
        'tilek': 'tilek',
        'country': dictionary,
        'house': my_house,
        'my_cars': list_of_cars,
        'null_value': null_value,
        'days': NUMBER_OF_DAYS,
        'today': today,
        'record_from_db': record_from_db,
        'text': 'Some text with үүүү.',
        'one_car': one_car
    }
    return render(request, 'journal/index.html', context)
