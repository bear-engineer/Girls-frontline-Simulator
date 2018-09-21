from rest_framework import serializers

from ..models import Doll


class DollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doll

        fields = (
            'doll_effect',
        )
