from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

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


@api_view(['GET', 'POST'])
def army_list(request, format=None):
    """
    List all armies, or create a new one
    """

    if request.method == 'GET':
        armies = Army.objects.all()
        serializer = ArmySerializer(armies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArmySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def army_detail(request, pk, format=None):
    """
    Retrieve, update or delete an army
    :param request:
    :param pk:
    :return:
    """

    try:
        army = Army.objects.get(pk=pk)
    except Army.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArmySerializer(army)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArmySerializer(army, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        army.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
