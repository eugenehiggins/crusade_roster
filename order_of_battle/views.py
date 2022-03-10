from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

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


@csrf_exempt
def army_list(request):
    """
    List all armies, or create a new one
    """

    if request.method == 'GET':
        armies = Army.objects.all()
        serializer = ArmySerializer(armies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArmySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def army_detail(request, pk):
    """
    Retrieve, update or delete an army
    :param request:
    :param pk:
    :return:
    """

    try:
        army = Army.objects.get(pk=pk)
    except Army.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArmySerializer(army)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArmySerializer(army, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        army.delete()
        return HttpResponse(status=204)
