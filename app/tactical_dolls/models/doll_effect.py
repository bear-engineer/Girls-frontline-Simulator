from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from .doll import Doll

__all__ = (
    'DollEffect',
    'DollEffectGrid',
)


class DollEffect(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_effect',
        blank=True
    )

    effect_type = models.CharField(max_length=100, blank=True, null=True)
    effect_center = models.PositiveSmallIntegerField(blank=True, null=True)
    effect_pos = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True,
                                  null=True)

    def __str__(self):
        return self.effect_pos


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
