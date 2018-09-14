from django.contrib import admin

# Register your models here.
from .models import (
    Doll,
    DollSkinImage,
    DollDrop,
    DollSDImage,
    DollEffectPos,
    DollEffectGrid,
    DollEffectType,
    DollSkill,
)

admin.site.register(Doll)
admin.site.register(DollSkinImage)
admin.site.register(DollSDImage)
admin.site.register(DollDrop)
admin.site.register(DollEffectPos)
admin.site.register(DollEffectGrid)
admin.site.register(DollEffectType)
admin.site.register(DollSkill)
