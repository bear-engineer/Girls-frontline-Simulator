from rest_framework import serializers

from equip.models import Equip


class EquipListSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()

    class Meta:
        model = Equip
        fields = (
            'id',
            'code_name',
            'type',
            'rank',
            'image',
        )
