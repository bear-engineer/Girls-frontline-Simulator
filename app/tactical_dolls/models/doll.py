from django.core.validators import validate_comma_separated_integer_list
from django.db import models

__all__ = (
    'Doll',
)


class Doll(models.Model):
    """
    전술 인형 정보
    """
    RANK_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    TYPE_CHOICE = (
        ('hg', 'hg'),
        ('ar', 'ar'),
        ('smg', 'smg'),
        ('sg', 'sg'),
        ('mg', 'mg'),
        ('rf', 'rf'),
    )

    COOLDOWN_TYPE = (
        ('frame', 'frame'),
        ('turn', 'turn')
    )

    id = models.PositiveSmallIntegerField(unique=True, primary_key=True, verbose_name='전술 인형 넘버링')
    rank = models.CharField(max_length=1, choices=RANK_CHOICE, verbose_name='전술 인형 등급')
    type = models.CharField(max_length=3, choices=TYPE_CHOICE, verbose_name='전술 인형 타입')
    buildtime = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='전술 인형 제조 시간')
    codename = models.CharField(max_length=50, blank=True, null=True, verbose_name='전술 인형 명칭')
    grow = models.PositiveSmallIntegerField(blank=True, null=True)
    skill01_id = models.PositiveSmallIntegerField(blank=True, null=True)
    skill01_codename = models.PositiveSmallIntegerField(blank=True, null=True)
    skill01_cooldowntype = models.CharField(choices=COOLDOWN_TYPE, blank=True, null=True)
    skill01_initialcooldown = models.PositiveSmallIntegerField(blank=True, null=True)
    skill01_consumption = models.PositiveSmallIntegerField(blank=True, null=True)
    skill02_id = models.PositiveSmallIntegerField(blank=True, null=True)
    skill02_codename = models.PositiveSmallIntegerField(blank=True, null=True)
    skill02_cooldowntype = models.CharField(choices=COOLDOWN_TYPE, blank=True, null=True)
    skill02_initialcooldown = models.PositiveSmallIntegerField(blank=True, null=True)
    skill02_consumption = models.PositiveSmallIntegerField(blank=True, null=True)
    obtain = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True)
    equip01 = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True)
    equip02 = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True)
    equip03 = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True)
    mindupdata = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True,
                                  null=True)

    def __str__(self):
        return f'No.{self.id} Type.{self.type} CodeName.{self.codename}'
