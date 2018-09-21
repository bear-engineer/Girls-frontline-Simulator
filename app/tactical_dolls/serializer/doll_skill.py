from rest_framework import serializers

from ..models import DollSkill01, DollSkill02

__all__ = (
    'DollSkillSerializer01',
    'DollSkillSerializer02',
)


class DollSkillSerializer01(serializers.ModelSerializer):
    class Meta:
        model = DollSkill01
        fields = '__all__'


class DollSkillSerializer02(serializers.ModelSerializer):
    class Meta:
        model = DollSkill02
        fields = '__all__'
