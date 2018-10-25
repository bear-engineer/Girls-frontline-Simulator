from django.db import models


# Create your models here.
# 'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/equip.json'
class DollEquip(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    codename = models.CharField(max_length=30, blank=True, null=True)
    kr_name = models.CharField(max_length=30, blank=True, null=True)
    rank = models.PositiveSmallIntegerField(blank=True, null=True)
    equip_image = models.ImageField(upload_to='equip_image', blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    company = models.CharField(max_length=30, blank=True, null=True)
    exclusiveRate = models.PositiveIntegerField(blank=True, null=True)
    maxLevel = models.PositiveIntegerField(blank=True, null=True)
    build_time = models.PositiveIntegerField(blank=True, null=True)
    is_private = models.BooleanField(blank=True, null=True)


class DollEquipStatus(models.Model):
    equip = models.ForeignKey(
        DollEquip,
        on_delete=models.CASCADE,
        related_name='doll_equip_status',
    )
    pow = models.SmallIntegerField(blank=True, null=True)
    hit = models.SmallIntegerField(blank=True, null=True)
    rate = models.SmallIntegerField(blank=True, null=True)
    dodge = models.SmallIntegerField(blank=True, null=True)
    armor = models.SmallIntegerField(blank=True, null=True)
    bullet = models.SmallIntegerField(blank=True, null=True)
    critical_percent = models.SmallIntegerField(blank=True, null=True)
    critical_harm_rate = models.SmallIntegerField(blank=True, null=True)
    speed = models.SmallIntegerField(blank=True, null=True)
    night_view = models.SmallIntegerField(blank=True, null=True)
    armor_piercing = models.SmallIntegerField(blank=True, null=True)


class DollEquipFit(models.Model):
    equip = models.ForeignKey(
        DollEquip,
        on_delete=models.CASCADE,
        related_name='doll_equip_fit'
    )
    fit_doll_id = models.PositiveIntegerField(blank=True, null=True)
