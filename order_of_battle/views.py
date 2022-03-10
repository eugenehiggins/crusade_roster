from django.shortcuts import render, get_object_or_404
from django.template import loader
from rest_framework import status, mixins, generics

from order_of_battle.models import Unit, Army
from order_of_battle.serializers import ArmySerializer


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


class ArmyList(generics.ListCreateAPIView):
    """
    List all armies, or create a new one
    """
    queryset = Army.objects.all()
    serializer_class = ArmySerializer


class ArmyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an army
    :param request:
    :param pk:
    :return:
    """

    queryset = Army.objects.all()
    serializer_class = ArmySerializer



