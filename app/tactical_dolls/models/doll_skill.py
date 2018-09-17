from django.db import models
from .doll import Doll

__all__ = (
    'DollSkill01',
    'DollSkill02',
)


class DollSkill01(models.Model):
    """
    인형 스킬
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill_data01',
        blank=True,
    )

    level = models.PositiveSmallIntegerField(blank=True, null=True)
    cooldown = models.PositiveSmallIntegerField(blank=True, null=True)


class DollSkill02(models.Model):
    """
    인형 스킬
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill_data02',
        blank=True,
    )

    level = models.PositiveSmallIntegerField(blank=True, null=True)
    cooldown = models.PositiveSmallIntegerField(blank=True, null=True)
