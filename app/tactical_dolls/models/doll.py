from django.db import models

__all__ = (
    'Doll',
)


class Doll(models.Model):
    """
    전술 인형 정보
    """
    DOLL_TYPE = (
        ('hg', 'HG'),
        ('smg', 'SMG'),
        ('rf', 'RF'),
        ('ar', 'AR'),
        ('mg', 'MG'),
        ('sg', 'SG'),
    )
    DOLL_RATING = (
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
    )

    doll_id = models.PositiveIntegerField(verbose_name='인형 품번', primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='인형 이름')
    kr_name = models.CharField(max_length=50, verbose_name='인형 이름(한국어)', blank=True, null=True)
    rank = models.CharField(max_length=1, choices=DOLL_RATING, verbose_name='인형 등급', blank=True, null=True)
    type = models.CharField(max_length=3, choices=DOLL_TYPE, verbose_name='인형 유형', blank=True, null=True)
    illust = models.CharField(max_length=50, verbose_name='일러스트레이터', blank=True, null=True)
    voice = models.CharField(max_length=50, verbose_name='성우', blank=True, null=True)
    build_time = models.PositiveSmallIntegerField(verbose_name='제조 시간', blank=True, null=True)
    is_upgrade = models.BooleanField(verbose_name='개조', blank=True)

    # doll_thumbnail_image = models.ImageField(upload_to='doll_thumbnail_images', verbose_name='아이콘 일러스트')
    # doll_default_image = models.ImageField(upload_to='doll_default_images', verbose_name='기본 일러스트')
    # doll_damage_image = models.ImageField(upload_to='doll_damage_images', verbose_name='파손 일러스트')
    # doll_Introduce = models.TextField(max_length=255, verbose_name='소개', blank=True)
