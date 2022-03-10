from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from order_of_battle.models import Unit


def index(request):
    unit_list = Unit.objects.order_by('name')[:10]
    template = loader.get_template('unit/index.html')
    context = {
        'unit_list' : unit_list,
    }
    return render(request, 'unit/index.html', context)


def detail(request, id):
    unit = get_object_or_404(Unit, pk=id)
    return render(request, 'unit/detail.html', {'order_of_battle': unit})
