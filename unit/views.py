from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from unit.models import Unit


def index(request):
    unit_list = Unit.objects.order_by('name')[:10]
    template = loader.get_template('unit/index.html')
    context = {
        'unit_list' : unit_list,
    }
    return render(request, 'unit/index.html', context)


def detail(request, id):
    response = "Stats for unit %s"
    return HttpResponse(response % id)

