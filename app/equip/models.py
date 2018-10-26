from django.db import models
from app.doll.models import Doll


class Equip(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    code_name = models.CharField(max_length=50)
    rank = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    exclusive_rate = models.PositiveIntegerField()
    max_level = models.PositiveSmallIntegerField()
    build_time = models.PositiveIntegerField()
    is_private = models.BooleanField(default=False)
    pow = models.SmallIntegerField()
    hit = models.SmallIntegerField()
    rate = models.SmallIntegerField()
    dodge = models.SmallIntegerField()
    armor = models.SmallIntegerField()
    bullet = models.SmallIntegerField()
    critical_percent = models.SmallIntegerField()
    critical_harm_rate = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    night_view = models.SmallIntegerField()
    armor_piercing = models.SmallIntegerField()
    private_field = models.ManyToManyField(
        'self',
        through='EquipPrivate',
        through_fields=('equip', 'doll'),
    )


class EquipPrivate(models.Model):
    equip = models.ForeignKey(
        'Equip',
        on_delete=models.CASCADE
    )
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE
    )
