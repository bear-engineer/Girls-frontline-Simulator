from django.contrib import admin

# Register your models here.
from .models import (
    Dolls as Doll,
    DollsSkinImage,
    DollsDrop,
    DollsSDImage,
    DollsEffectPos,
    DollsEffectGrid,
    DollsEffectType,
    DollsSkill,
)

admin.site.register(Doll)
admin.site.register(DollsSkinImage)
admin.site.register(DollsSDImage)
admin.site.register(DollsDrop)
admin.site.register(DollsEffectPos)
admin.site.register(DollsEffectGrid)
admin.site.register(DollsEffectType)
admin.site.register(DollsSkill)
