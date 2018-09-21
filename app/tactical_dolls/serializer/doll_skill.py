from rest_framework import serializers

from ..models import DollSkill01, DollSkill02

__all__ = (
    'DollSkillSerializer01',
    'DollSkillSerializer02',
)


class DollSkillSerializer01(serializers.ModelSerializer):
    skill_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DollSkill01
        fields = '__all__'

    def get_skill_data(self, obj):
        return eval(obj.skill_data)


class DollSkillSerializer02(serializers.ModelSerializer):
    skill_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DollSkill02
        fields = '__all__'

    def get_skill_data(self, obj):
        return eval(obj.skill_data)

