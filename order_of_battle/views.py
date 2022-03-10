from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ArmyList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.ListCreateAPIView):
    """
    List all armies, or create a new one
    """
    queryset = Army.objects.all()
    serializer_class = ArmySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArmyDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve, update or delete an army
    :param request:
    :param pk:
    :return:
    """

    queryset = Army.objects.all()
    serializer_class = ArmySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


