from django.db import models

from .doll import Doll

__all__ = (
    'DollStatus',
)


class DollStatus(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_status',
    )
    armor = models.PositiveSmallIntegerField(verbose_name='장갑', blank=True)
    dodge = models.PositiveSmallIntegerField(verbose_name='회피', blank=True)
    hit = models.PositiveSmallIntegerField(verbose_name='명중', blank=True)
    hp = models.PositiveSmallIntegerField(verbose_name='체력', blank=True)
    pow = models.PositiveSmallIntegerField(verbose_name='화력', blank=True)
    range = models.PositiveSmallIntegerField(verbose_name='사거리(철혈)', blank=True)
    rate = models.PositiveSmallIntegerField(verbose_name='사속', blank=True)
    shield = models.PositiveSmallIntegerField(verbose_name='보호막(철혈)', blank=True)
    speed = models.PositiveSmallIntegerField(verbose_name='이동속도', blank=True)
    crit = models.PositiveSmallIntegerField(verbose_name='크리티컬 확률(%)', blank=True)
    critdmg = models.PositiveSmallIntegerField(verbose_name='크리티컬 데미지 추가 증가량(%)', blank=True)
    armor_piercing = models.PositiveSmallIntegerField(verbose_name='장갑 관통', blank=True)
    night_view = models.PositiveSmallIntegerField(verbose_name='야간 명중률(%)', blank=True, null=True, default=0)
    cool_down = models.PositiveSmallIntegerField(verbose_name='쿨타임 감소(%)', blank=True, null=True, default=0)
    bullet = models.PositiveSmallIntegerField(verbose_name='장탄 수', blank=True)
