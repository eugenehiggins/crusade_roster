from django.contrib.auth.models import User
from rest_framework import serializers

from order_of_battle.models import Army, Unit, Weapon


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name', 'range', 'type', 'strength']


class UnitSerializer(serializers.ModelSerializer):
    weapons = WeaponSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = ['id', 'name', 'power', 'crusade_points', 'xp', 'weapons']


class ArmySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Army
        fields = ['url', 'id', 'owner', 'name', 'general', 'battles', 'units']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    armies = serializers.HyperlinkedRelatedField(
        many=True, view_name='army-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'armies']
