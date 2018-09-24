from django.db import models

from .doll import Doll

__all__ = (
    'DollStatus',
)


class DollStatus(models.Model):
    """
    인형 능력치
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_status',
    )
    hp = models.PositiveSmallIntegerField(blank=True, null=True)
    pow = models.PositiveSmallIntegerField(blank=True, null=True)
    hit = models.PositiveSmallIntegerField(blank=True, null=True)
    dodge = models.PositiveSmallIntegerField(blank=True, null=True)
    speed = models.PositiveSmallIntegerField(blank=True, null=True)
    rate = models.PositiveSmallIntegerField(blank=True, null=True)
    armor_piercing = models.PositiveSmallIntegerField(blank=True, null=True)
    critical_percent = models.PositiveSmallIntegerField(blank=True, null=True)
    bullet = models.PositiveSmallIntegerField(blank=True, null=True)
