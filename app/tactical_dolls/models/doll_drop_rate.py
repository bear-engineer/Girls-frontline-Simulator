from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from .doll import Doll

__all__ = (
    'DollDrop',
)


class DollDrop(models.Model):
    """
    인형 획득 위치
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_drop',
        blank=True,
    )
    drop_field = models.CharField(validators=[validate_comma_separated_integer_list], max_length=30,
                                  verbose_name='Drop Fields', blank=True, null=True)
