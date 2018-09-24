from django.core.validators import validate_comma_separated_integer_list
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
        blank=True
    )
    type = models.CharField(max_length=100, blank=True, null=True)
    center = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.type} {self.center}'


class DollEffectPos(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_pos',
        blank=True
    )
    pos = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.pos


class DollEffectGrid(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect_grid',
        blank=True
    )
    pow = models.PositiveSmallIntegerField(blank=True, null=True)
    hit = models.PositiveSmallIntegerField(blank=True, null=True)
    rate = models.PositiveSmallIntegerField(blank=True, null=True)
    dodge = models.PositiveSmallIntegerField(blank=True, null=True)
    criticalpercent = models.PositiveSmallIntegerField(blank=True, null=True)
    cooldown = models.PositiveSmallIntegerField(blank=True, null=True)
    armor = models.PositiveSmallIntegerField(blank=True, null=True)
