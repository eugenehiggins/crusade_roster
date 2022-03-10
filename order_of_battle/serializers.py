from django.contrib.auth.models import User
from rest_framework import serializers

from order_of_battle.models import Army


class ArmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Army
        fields = ['id', 'name', 'general', 'battles']


class UserSerializer(serializers.ModelSerializer):
    armies = serializers.PrimaryKeyRelatedField(many=True, queryset=Army.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
