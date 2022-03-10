from rest_framework import serializers

from order_of_battle.models import Army


class ArmySerializer(serializers.ModelSerializer):
    class Meta:
        model = Army
        fields = ['id', 'name', 'general', 'battles']