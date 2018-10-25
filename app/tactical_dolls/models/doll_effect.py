from django.db import models
from .doll import Doll

__all__ = (
    'DollEffect',
    'DollEffectPos',
    'DollEffectGrid',
)


class DollEffect(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect',
    )
    type = models.CharField(max_length=100, blank=True, null=True)
    center = models.PositiveIntegerField(blank=True, null=True)


class DollEffectPos(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_pos',
        blank=True
    )
    pos = models.PositiveIntegerField(blank=True, null=True)


class DollEffectGrid(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_grid',
        blank=True
    )
    pow = models.PositiveIntegerField(blank=True, null=True)
    hit = models.PositiveIntegerField(blank=True, null=True)
    rate = models.PositiveIntegerField(blank=True, null=True)
    dodge = models.PositiveIntegerField(blank=True, null=True)
    critical_percent = models.PositiveIntegerField(blank=True, null=True)
    cool_down = models.PositiveIntegerField(blank=True, null=True)
    armor = models.PositiveIntegerField(blank=True, null=True)
