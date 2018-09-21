from rest_framework import serializers

from ..models import DollEffect


class DollSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollEffect

        fields = (
            'doll_effect',
        )