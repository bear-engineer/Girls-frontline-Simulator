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

    id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    rank = models.CharField(max_length=1, choices=RANK_CHOICE)
    type = models.CharField(max_length=3, choices=TYPE_CHOICE)
    buildtime = models.PositiveSmallIntegerField(blank=True, null=True)
    codename = models.CharField(max_length=50, blank=True, null=True)
