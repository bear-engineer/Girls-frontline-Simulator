from django.core.validators import validate_comma_separated_integer_list
from django.db import models

from .managers import Update

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
        ('7', 'extra')
    )

    TYPE_CHOICE = (
        ('hg', 'hg'),
        ('ar', 'ar'),
        ('smg', 'smg'),
        ('sg', 'sg'),
        ('mg', 'mg'),
        ('rf', 'rf'),
    )

    id = models.PositiveSmallIntegerField(unique=True, primary_key=True, verbose_name='전술 인형 넘버링')
    codename = models.CharField(max_length=50, blank=True, null=True, verbose_name='전술 인형 명칭')
    kr_name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.CharField(max_length=5, choices=RANK_CHOICE, verbose_name='전술 인형 등급')
    type = models.CharField(max_length=3, choices=TYPE_CHOICE, verbose_name='전술 인형 타입')
    build_time = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='전술 인형 제조 시간')
    grow = models.PositiveSmallIntegerField(blank=True, null=True)
    obtain = models.CharField(validators=[validate_comma_separated_integer_list], max_length=50, blank=True, null=True)
    is_upgrade = models.BooleanField()

    objects = models.Manager()
    object = Update()

    def __str__(self):
        return f'No.{self.id} Type.{self.type} CodeName.{self.codename}'
