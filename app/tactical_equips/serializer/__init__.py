from rest_framework import serializers

from ..models import DollEquip


class EquipSerializer(serializers.ModelSerializer):
    is_private = serializers.NullBooleanField()

    class Meta:
        model = DollEquip
        fields = '__all__'
