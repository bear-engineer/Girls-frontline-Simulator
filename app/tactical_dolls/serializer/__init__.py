from rest_framework import serializers
from ..models import Doll, DollEffect, DollEffectPos, DollDetail
from .doll_skill import *
from .doll_status import *


class DollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doll
        fields = (
            'id',
            'codename',
            'type',
            'rank',
            'image',
        )


class DollContextSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollDetail
        fields = '__all__'


class DollDetailSerializer(serializers.ModelSerializer):
    doll_detail = DollContextSerializer(many=True, read_only=True)

    class Meta:
        model = Doll
        fields = '__all__'
