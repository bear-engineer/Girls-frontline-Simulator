from django.db import models
from .doll import Doll

__all__ = (
    'DollSkill01',
    'DollSkill02',
    'DollSkillData01',
    'DollSkillData02',
)

COOL_DOWN_TYPE = (
    ('frame', 'frame'),
    ('turn', 'turn')
)


class DollSkill01(models.Model):
    """
    인형 스킬
    """

    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill01',
        blank=True,
    )
    skill_id = models.PositiveIntegerField(blank=True, null=True)
    codename = models.CharField(max_length=50, blank=True, null=True)
    cool_down_type = models.CharField(max_length=50, choices=COOL_DOWN_TYPE, blank=True, null=True)
    initial_cool_down = models.PositiveIntegerField(blank=True, null=True)
    consumption = models.PositiveIntegerField(blank=True, null=True)


class DollSkill02(models.Model):
    """
    인형 스킬
    """
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill02',
        blank=True,
    )

    skill_id = models.PositiveIntegerField(blank=True, null=True)
    skill_image = models.ImageField(upload_to='doll_skill_images', blank=True, null=True)
    codename = models.CharField(max_length=50, blank=True, null=True)
    cool_down_type = models.CharField(max_length=50, choices=COOL_DOWN_TYPE, blank=True, null=True)
    initial_cool_down = models.PositiveIntegerField(blank=True, null=True)
    consumption = models.PositiveIntegerField(blank=True, null=True)


class DollSkillData01(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill01_data',
        blank=True,
    )
    level = models.PositiveIntegerField(blank=True, null=True)
    cool_down = models.PositiveIntegerField(blank=True, null=True)


class DollSkillData02(models.Model):
    doll = models.ForeignKey(
        Doll,
        on_delete=models.CASCADE,
        related_name='doll_skill02_data',
        blank=True,
    )
    level = models.PositiveIntegerField(blank=True, null=True)
    cool_down = models.PositiveIntegerField(blank=True, null=True)
