from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from .doll import Doll

__all__ = (
    'DollSkill01',
    'DollSkill02',
)

COOLDOWN_TYPE = (
    ('frame', 'frame'),
    ('turn', 'turn')
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
    skill_id = models.PositiveSmallIntegerField(blank=True, null=True)
    codename = models.CharField(max_length=50, blank=True, null=True)
    cooldowntype = models.CharField(max_length=4, choices=COOLDOWN_TYPE, blank=True, null=True)
    initialcooldown = models.PositiveSmallIntegerField(blank=True, null=True)
    consumption = models.PositiveSmallIntegerField(blank=True, null=True)
    skill_data = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True,
                                  null=True)


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

    skill_id = models.PositiveSmallIntegerField(blank=True, null=True)
    codename = models.CharField(max_length=50, blank=True, null=True)
    cooldowntype = models.CharField(max_length=4, choices=COOLDOWN_TYPE, blank=True, null=True)
    initialcooldown = models.PositiveSmallIntegerField(blank=True, null=True)
    consumption = models.PositiveSmallIntegerField(blank=True, null=True)
    skill_data = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True,
                                  null=True)
