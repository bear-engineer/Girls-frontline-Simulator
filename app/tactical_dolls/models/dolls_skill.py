from django.db import models
from .dolls import Dolls

__all__ = (
    'DollsSkill',
)


class DollsSkill(models.Model):
    doll = models.ForeignKey(
        Dolls,
        on_delete=models.CASCADE,
        related_name='doll_skill',
        blank=True,
    )
