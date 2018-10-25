from django.db import models

from .doll import Doll

__all__ = (
    'DollStatus',
)


class DollStatus(models.Model):
    """
    인형 능력치
    Default Status Lv 100, Fav 100, Dummy 5Link
    site data, json data 분리
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_status',
    )

    # 1번 크롤러
    hp = models.PositiveIntegerField(blank=True, null=True)
    pow = models.PositiveIntegerField(blank=True, null=True)
    hit = models.PositiveIntegerField(blank=True, null=True)
    dodge = models.PositiveIntegerField(blank=True, null=True)
    rate = models.PositiveIntegerField(blank=True, null=True)

    # 2번 크롤러
    speed = models.PositiveIntegerField(blank=True, null=True)
    armor_piercing = models.PositiveIntegerField(blank=True, null=True)
    critical_harm_rate = models.PositiveIntegerField(blank=True, null=True)
    critical_percent = models.PositiveIntegerField(blank=True, null=True)
    bullet = models.PositiveIntegerField(blank=True, null=True)
    night_view = models.PositiveIntegerField(blank=True, null=True)
    armor = models.PositiveIntegerField(blank=True, null=True)
