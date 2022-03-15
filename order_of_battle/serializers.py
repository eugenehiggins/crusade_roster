from django.contrib.auth.models import User
from rest_framework import serializers

from order_of_battle.models import Army


class ArmySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Army
        fields = ['url', 'id', 'owner', 'name', 'general', 'battles']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    armies = serializers.HyperlinkedRelatedField(
        many=True, view_name='army-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'armies']
