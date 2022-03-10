from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from rest_framework import status
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


class ArmyList(APIView):
    """
    List all armies, or create a new one
    """

    def get(self, request, format=None):
        armies = Army.objects.all()
        serializer = ArmySerializer(armies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArmySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArmyDetail(APIView):
    """
    Retrieve, update or delete an army
    :param request:
    :param pk:
    :return:
    """

    def get_object(self, pk):
        try:
            return Army.objects.get(pk=pk)
        except Army.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        army = self.get_object(pk)
        serializer = ArmySerializer(army)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        army = self.get_object(pk)
        serializer = ArmySerializer(army, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        army = self.get_object(pk)
        army.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
