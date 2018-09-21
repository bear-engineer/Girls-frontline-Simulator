from rest_framework import serializers

from ..models import DollStatus

__all__ = (
    'DollStatusSerializer',
)


class DollStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollStatus
        exclude = ('id', 'doll')
