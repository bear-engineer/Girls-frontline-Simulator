from django.db import models

from .dolls import Dolls

__all__ = (
    'DollsStatus',
)


class DollsStatus(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_status',
    )
    doll_armor = models.PositiveSmallIntegerField(verbose_name='장갑', blank=True)
    doll_dodge = models.PositiveSmallIntegerField(verbose_name='회피', blank=True)
    doll_hit = models.PositiveSmallIntegerField(verbose_name='명중', blank=True)
    doll_hp = models.PositiveSmallIntegerField(verbose_name='체력', blank=True)
    doll_pow = models.PositiveSmallIntegerField(verbose_name='화력', blank=True)
    doll_range = models.PositiveSmallIntegerField(verbose_name='사거리(철혈)', blank=True)
    doll_rate = models.PositiveSmallIntegerField(verbose_name='사속', blank=True)
    doll_shield = models.PositiveSmallIntegerField(verbose_name='보호막(철혈)', blank=True)
    doll_speed = models.PositiveSmallIntegerField(verbose_name='이동속도', blank=True)
    doll_crit = models.PositiveSmallIntegerField(verbose_name='크리티컬 확률(%)', blank=True)
    doll_critdmg = models.PositiveSmallIntegerField(verbose_name='크리티컬 데미지 추가 증가량(%)', blank=True)
    doll_armorpiercing = models.PositiveSmallIntegerField(verbose_name='장갑 관통', blank=True)
    doll_nightview = models.PositiveSmallIntegerField(verbose_name='야간 명중률(%)', blank=True, null=True, default=0)
    doll_cooldown = models.PositiveSmallIntegerField(verbose_name='쿨타임 감소(%)', blank=True, null=True, default=0)
    doll_bullet = models.PositiveSmallIntegerField(verbose_name='장탄 수', blank=True)
