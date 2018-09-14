from django.db import models
from .dolls import Dolls

__all__ = (
    'DollsDrop',
)


class DollsDrop(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_drop',
        blank=True,
    )
    doll_drop_field = models.CharField(max_length=30, blank=True, verbose_name='Drop Fields')
