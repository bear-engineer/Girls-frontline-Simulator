from django.db import models
from .doll import Doll

__all__ = (
    'DollDrop',
)


class DollDrop(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_drop',
        blank=True,
    )
    drop_field = models.CharField(max_length=30, blank=True, verbose_name='Drop Fields')
