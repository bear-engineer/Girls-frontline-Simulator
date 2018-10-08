from django.db import models
from .doll import Doll

__all__ = (
    'DollDetail',
)


class DollDetail(models.Model):
    """
    전술인형 상세정보
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_detail'
    )
    drop = models.TextField(max_length=255, blank=True, null=True)
    context = models.TextField(max_length=255, blank=True, null=True)
