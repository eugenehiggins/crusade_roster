from django.contrib.auth.models import User
# from django.shortcuts import render, get_object_or_404
# from django.template import loader
from rest_framework import permissions, viewsets, renderers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action

from order_of_battle.models import Army
from order_of_battle.permissions import IsOwnerOrReadOnly
from order_of_battle.serializers import ArmySerializer, UserSerializer


# def index(request):
#     unit_list = Unit.objects.order_by('name')[:10]
#     template = loader.get_template('unit/index.html')
#     context = {
#         'unit_list' : unit_list,
#     }
#     return render(request, 'unit/index.html', context)
#
#
# def detail(request, id):
#     unit = get_object_or_404(Unit, pk=id)
#     return render(request, 'unit/detail.html', {'order_of_battle': unit})


class ArmyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """

    queryset = Army.objects.all()
    serializer_class = ArmySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'armies': reverse('army-list', request=request, format=format)
    })


