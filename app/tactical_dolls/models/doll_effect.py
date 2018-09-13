from django.db import models
from .dolls import Dolls

__all__ = (
    'DollsEffectType',
    'DollsEffectGrid',
    'DollsEffectPos',
)


class DollsEffectType(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_effect_type',
        blank=True
    )

    effect_type = models.CharField(max_length=50, blank=True)
    effect_center = models.PositiveSmallIntegerField()


class DollsEffectPos(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_effect_pos',
        blank=True
    )
    effect_pos = models.PositiveSmallIntegerField()


class DollsEffectGrid(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_effect_grid',
        blank=True
    )
    effect_pw = models.PositiveSmallIntegerField()
    effect_dr = models.PositiveSmallIntegerField()
    effect_cd = models.PositiveSmallIntegerField()
    effect_ic = models.PositiveSmallIntegerField()
