from django.db import models

from tactical_dolls.models import Doll

__all__ = (
    'DollMindUpdate',
)


class DollMindUpdate(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_mind_update'
    )
    core = models.PositiveSmallIntegerField(blank=True, null=True)
    mind_piece = models.PositiveSmallIntegerField(blank=True, null=True)
