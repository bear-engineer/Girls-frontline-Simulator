from django.db import models
from .dolls import Dolls

__all__ = (
    'DollsSkinImage',
    'DollsSDImage',
)


class DollsSkinImage(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_skins',
        blank=True
    )
    doll_skin_name = models.CharField(max_length=50, blank=True, verbose_name='스킨 이름')
    doll_skin_story = models.TextField(max_length=255, blank=True, verbose_name='스킨 스토리')
    doll_sd_skin = models.ImageField(upload_to='doll_sd_skins', blank=True, verbose_name='스킨 SD 일러스트')
    doll_default_skin = models.ImageField(upload_to='doll_default_skins', blank=True, verbose_name='스킨 기본 일러스트')
    doll_damage_skin = models.ImageField(upload_to='doll_damage_skins', blank=True, verbose_name='스킨 파손 일러트스')


class DollsSDImage(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_sd',
        blank=True
    )
    doll_sd_wait_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 기본 일러스트')
    doll_sd_attack_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 공격 일러스트')
    doll_sd_die_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 파손 일러스트')
    doll_sd_move_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 이동 일러스트')
    doll_sd_victory1_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 승리1 일러스트')
    doll_sd_victory2_image = models.ImageField(upload_to='doll_sd_image', blank=True, verbose_name='SD 승리2 일러스트')