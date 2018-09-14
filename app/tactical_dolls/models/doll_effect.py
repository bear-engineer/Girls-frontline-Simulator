from django.db import models
from .doll import Doll

__all__ = (
    'DollEffectType',
    'DollEffectGrid',
    'DollEffectPos',
)


class DollEffectType(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_type',
        blank=True
    )

    effect_type = models.CharField(max_length=50, blank=True)
    effect_center = models.PositiveSmallIntegerField()


class DollEffectPos(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_pos',
        blank=True
    )
    effect_pos = models.PositiveSmallIntegerField()


class DollEffectGrid(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_grid',
        blank=True
    )
    effect_pw = models.PositiveSmallIntegerField()
    effect_dr = models.PositiveSmallIntegerField()
    effect_cd = models.PositiveSmallIntegerField()
    effect_ic = models.PositiveSmallIntegerField()
