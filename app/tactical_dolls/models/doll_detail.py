from django.db import models
from .doll import Doll

__all__ = (
    'DollDetail',
)


class DollDetail(models.Model):
    """
    전술인형 context
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_detail'
    )
    drop = models.TextField(blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)
    dialogue1 = models.CharField(max_length=200, blank=True, null=True)
    dialogue2 = models.CharField(max_length=200, blank=True, null=True)
    dialogue3 = models.CharField(max_length=200, blank=True, null=True)
    soul_contract = models.TextField(blank=True, null=True)
    gain = models.CharField(max_length=200, blank=True, null=True)
