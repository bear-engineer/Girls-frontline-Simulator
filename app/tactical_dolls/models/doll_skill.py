from django.db import models
from .doll import Doll

__all__ = (
    'DollSkill',
)


class DollSkill(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill',
        blank=True,
    )



