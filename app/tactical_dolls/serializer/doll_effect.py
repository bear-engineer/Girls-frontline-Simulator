from rest_framework import serializers

from ..models import DollEffect, DollEffectGrid

__all__ = (
    'DollEffectSerializer',
    'DollEffectGridSerializer',
)


class DollEffectSerializer(serializers.ModelSerializer):
    effectpos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DollEffect
        exclude = ('doll', 'id')

    def get_effectpos(self, obj):
        return eval(obj.effectpos)


class DollEffectGridSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollEffectGrid
        exclude = ('doll', 'id',)
