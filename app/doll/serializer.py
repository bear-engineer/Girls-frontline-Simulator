from django.conf import settings
from rest_framework import serializers

from doll.models import Doll


class DollListSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField()

    class Meta:
        model = Doll
        fields = (
            'id',
            'code_name',
            'type',
            'rank',
            'image',
        )
