from django.db import models

__all__ = (
    'Dolls',
)


class Dolls(models.Model):
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

    doll_id = models.PositiveIntegerField(verbose_name='인형 품번')
    doll_name = models.CharField(max_length=50, verbose_name='인형 이름')
    doll_krname = models.CharField(max_length=50, verbose_name='인형 이름(한국어)', blank=True, null=True)
    doll_rank = models.CharField(max_length=1, choices=DOLL_RATING, verbose_name='인형 등급', blank=True, null=True)
    doll_type = models.CharField(max_length=3, choices=DOLL_TYPE, verbose_name='인형 유형', blank=True, null=True)
    doll_illust = models.CharField(max_length=50, verbose_name='일러스트레이터', blank=True, null=True)
    doll_voice = models.CharField(max_length=50, verbose_name='성우', blank=True, null=True)
    doll_buildtime = models.PositiveSmallIntegerField(verbose_name='제조 시간', blank=True, null=True)
    doll_is_upgrade = models.BooleanField(default=False, verbose_name='개조', blank=True)
    # doll_thumbnail_image = models.ImageField(upload_to='doll_thumbnail_images', verbose_name='아이콘 일러스트')
    # doll_default_image = models.ImageField(upload_to='doll_default_images', verbose_name='기본 일러스트')
    # doll_damage_image = models.ImageField(upload_to='doll_damage_images', verbose_name='파손 일러스트')
    # doll_Introduce = models.TextField(max_length=255, verbose_name='소개', blank=True)
