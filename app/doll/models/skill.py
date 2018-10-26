from django.db import models

__all__ = (
    'Skill',
    'SkillData',
)


class Skill(models.Model):
    doll = models.ForeignKey(
        'Doll',
        on_delete=models.CASCADE,
    )
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    code_name = models.CharField(max_length=50)
    skill_type = models.CharField(max_length=30)
    skill_image = models.ImageField(upload_to='skill_image', blank=True, null=True)
    cool_down_type = models.CharField(max_length=30)
    initial_cool_down = models.PositiveIntegerField()
    consumption = models.PositiveIntegerField()


class SkillData(models.Model):
    skill = models.ForeignKey(
        'Skill',
        on_delete=models.CASCADE,
    )
    level = models.PositiveSmallIntegerField()
    cool_down = models.PositiveIntegerField()
