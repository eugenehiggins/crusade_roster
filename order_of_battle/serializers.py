from rest_framework import serializers

from order_of_battle.models import Army


class ArmySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    general = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data):
        return Army.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.general = validated_data.get('general', instance.general)
        return instance
