from django.db import models

from .doll import Doll

__all__ = (
    'DollEquipSlot01',
    'DollEquipSlot02',
    'DollEquipSlot03',
)


class DollEquipSlot01(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_equip_slot01'
    )
    module = models.CharField(max_length=60, blank=True, null=True)


class DollEquipSlot02(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_equip_slot02'
    )
    module = models.CharField(max_length=60, blank=True, null=True)


class DollEquipSlot03(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_equip_slot03'
    )
    module = models.CharField(max_length=60, blank=True, null=True)
