from django.db import models
from .doll import Doll

__all__ = (
    'DollImage',
    # 'DollSkinImage',
)


class DollImage(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_image',

    )
    default_skin = models.ImageField(upload_to='doll_default_skins', blank=True, verbose_name='기본 일러스트')
    # damage_skin = models.ImageField(upload_to='doll_damage_skins', blank=True, verbose_name='파손 일러트스')


# class DollSkinImage(models.Model):
#     """
#     인형 이미지 스킨
#     """
#     doll = models.ForeignKey(
#         Doll,
#         on_delete=models.CASCADE,
#         related_name='doll_skins',
#         blank=True
#     )
#     skin_name = models.CharField(max_length=50, blank=True, verbose_name='스킨 이름')
#     default_skin = models.ImageField(upload_to='doll_default_skins', blank=True, verbose_name='스킨 기본 일러스트')
#     damage_skin = models.ImageField(upload_to='doll_damage_skins', blank=True, verbose_name='스킨 파손 일러트스')
