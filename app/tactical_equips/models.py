from django.db import models


# Create your models here.
# 'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/equip.json'
class DollEquip(models.Model):
    id = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    codename = models.CharField(max_length=30, blank=True, null=True)
    kr_name = models.CharField(max_length=30, blank=True, null=True)
    rank = models.PositiveSmallIntegerField(blank=True, null=True)
    equip_image = models.ImageField(upload_to='equip_image', blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    company = models.CharField(max_length=5, blank=True, null=True)
    exclusiveRate = models.PositiveSmallIntegerField(blank=True, null=True)
    maxLevel = models.PositiveSmallIntegerField(blank=True, null=True)
    build_time = models.PositiveSmallIntegerField(blank=True, null=True)
    is_private = models.BooleanField(blank=True, null=True)


class DollEquipStatus(models.Model):
    equip = models.ForeignKey(
        DollEquip,
        on_delete=models.CASCADE,
        related_name='doll_equip_status',
    )
    pow = models.PositiveSmallIntegerField(blank=True, null=True)
    hit = models.PositiveSmallIntegerField(blank=True, null=True)
    rate = models.PositiveSmallIntegerField(blank=True, null=True)
    dodge = models.PositiveSmallIntegerField(blank=True, null=True)
    armor = models.PositiveSmallIntegerField(blank=True, null=True)
    bullet = models.PositiveSmallIntegerField(blank=True, null=True)
    critical_percent = models.PositiveSmallIntegerField(blank=True, null=True)
    critical_harm_rate = models.PositiveSmallIntegerField(blank=True, null=True)
    speed = models.PositiveSmallIntegerField(blank=True, null=True)
    night_view = models.PositiveSmallIntegerField(blank=True, null=True)
    armor_piercing = models.PositiveSmallIntegerField(blank=True, null=True)


class DollEquipFit(models.Model):
    equip = models.ForeignKey(
        DollEquip,
        on_delete=models.CASCADE,
        related_name='doll_equip_fit'
    )
    fit_doll_id = models.PositiveSmallIntegerField(blank=True, null=True)
