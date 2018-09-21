from rest_framework import serializers
from ..models import Doll
from .doll_effect import *
from .doll_skill import *
from .doll_status import *


class DollSerializer(serializers.ModelSerializer):
    doll_effect = DollEffectSerializer(many=True)
    doll_skill_data01 = DollSkillSerializer01(many=True)
    doll_skill_data02 = DollSkillSerializer02(many=True)
    doll_status = DollStatusSerializer(many=True)

    class Meta:
        model = Doll

        fields = (
            'id',
            'rank',
            'buildtime',
            'codename',
            'grow',
            'doll_status',
            'doll_effect',
            'doll_skill_data01',
            'doll_skill_data02',
        )
