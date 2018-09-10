from django.db import models

pars_url = 'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'


class Dolls(models.Model):
    DOLL_TYPE = (
        ('HG', 'HG'),
        ('SM', 'SMG'),
        ('RF', 'RF'),
        ('AR', 'AR'),
        ('MG', 'MG'),
        ('SG', 'SG'),
    )
    DOLL_RATING = (
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
        # ('E', 'EXTRA'),
    )

    doll_no = models.PositiveIntegerField(verbose_name='인형 품번')
    doll_name = models.CharField(max_length=50, verbose_name='인형 이름')
    doll_type = models.CharField(max_length=2, choices=DOLL_TYPE, verbose_name='인형 유형')
    doll_rating = models.CharField(max_length=1, choices=DOLL_RATING, verbose_name='인형 등급')
    doll_thumbnail_image = models.ImageField(upload_to='doll_thumbnail_images', verbose_name='아이콘 일러스트')
    doll_default_image = models.ImageField(upload_to='doll_default_images', verbose_name='기본 일러스트')
    doll_damage_image = models.ImageField(upload_to='doll_damage_images', verbose_name='파손 일러스트')
    doll_Introduce = models.TextField(max_length=255, verbose_name='소개')
    doll_cv = models.CharField(max_length=50, blank=True, verbose_name='성우')
    doll_illustrator_creator = models.CharField(max_length=50, blank=True, verbose_name='일러스트레이터')
    doll_manufacturing_time = models.CharField(max_length=20, verbose_name='제조 시간')
    doll_is_upgrade = models.BooleanField(default=False, verbose_name='개조')
    doll_fp = models.PositiveSmallIntegerField(verbose_name='화력')
    doll_acc = models.PositiveSmallIntegerField(verbose_name='명중')
    doll_eva = models.PositiveSmallIntegerField(verbose_name='회피')
    doll_rof = models.PositiveSmallIntegerField(verbose_name='사속')
    doll_hp = models.PositiveSmallIntegerField(verbose_name='체력')
    doll_growth = models.PositiveSmallIntegerField(verbose_name='성장')


class DollsSkinImage(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_skins',
        blank=True
    )
    doll_skin_name = models.CharField(max_length=50, blank=True, verbose_name='스킨 이름')
    doll_skin_story = models.TextField(max_length=255, blank=True, verbose_name='스킨 스토리')
    doll_sd_skin = models.ImageField(upload_to='doll_sd_skins', verbose_name='스킨 SD 일러스트')
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


class DollsDrop(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_drop',
        blank=True
    )
    doll_drop_field = models.CharField(max_length=30, blank=True, verbose_name='Drop Fields')
