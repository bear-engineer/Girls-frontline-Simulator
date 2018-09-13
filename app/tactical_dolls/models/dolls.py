from django.db import models

__all__ = (
    'Dolls',
)


# 크롤링정보 요청 URL
# pars_url = 'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'


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

    doll_no = models.PositiveIntegerField(verbose_name='인형 품번')
    doll_name = models.CharField(max_length=50, verbose_name='인형 이름')
    doll_krname = models.CharField(max_length=50, verbose_name='인형 이름(한국어)', blank=True)
    doll_type = models.CharField(max_length=3, choices=DOLL_TYPE, verbose_name='인형 유형')
    doll_rating = models.CharField(max_length=1, choices=DOLL_RATING, verbose_name='인형 등급')
    doll_thumbnail_image = models.ImageField(upload_to='doll_thumbnail_images', verbose_name='아이콘 일러스트')
    doll_default_image = models.ImageField(upload_to='doll_default_images', verbose_name='기본 일러스트')
    doll_damage_image = models.ImageField(upload_to='doll_damage_images', verbose_name='파손 일러스트')
    doll_Introduce = models.TextField(max_length=255, verbose_name='소개', blank=True)
    doll_cv = models.CharField(max_length=50, blank=True, verbose_name='성우')
    doll_illustrator_creator = models.CharField(max_length=50, blank=True, verbose_name='일러스트레이터')
    doll_manufacturing_time = models.CharField(max_length=20, verbose_name='제조 시간', blank=True)
    doll_is_upgrade = models.BooleanField(default=False, verbose_name='개조', blank=True)
    doll_armor = models.PositiveSmallIntegerField(verbose_name='장갑', blank=True)
    doll_eva = models.PositiveSmallIntegerField(verbose_name='회피', blank=True)
    doll_acc = models.PositiveSmallIntegerField(verbose_name='명중', blank=True)
    doll_hp = models.PositiveSmallIntegerField(verbose_name='체력', blank=True)
    doll_fp = models.PositiveSmallIntegerField(verbose_name='화력', blank=True)
    doll_range = models.PositiveSmallIntegerField(verbose_name='사거리(철혈)', blank=True)
    doll_rate = models.PositiveSmallIntegerField(verbose_name='사속', blank=True)
    doll_shield = models.PositiveSmallIntegerField(verbose_name='보호막(철혈)', blank=True)
    doll_speed = models.PositiveSmallIntegerField(verbose_name='이동속도', blank=True)
    doll_crit = models.PositiveSmallIntegerField(verbose_name='크리티컬 확률(%)', blank=True)
    doll_critdmg = models.PositiveSmallIntegerField(verbose_name='크리티컬 데미지 추가 증가량(%)', blank=True)
    doll_armorpiercing = models.PositiveSmallIntegerField(verbose_name='장갑 관통', blank=True)
    doll_nightview = models.PositiveSmallIntegerField(verbose_name='야간 명중률(%)', blank=True)
    doll_cooldown = models.PositiveSmallIntegerField(verbose_name='쿨타임 감소(%)', blank=True)
    doll_bullet = models.PositiveSmallIntegerField(verbose_name='장탄 수', blank=True)
