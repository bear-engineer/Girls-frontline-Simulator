from django.contrib import admin

# Register your models here.
from .models import (
    Doll,
    DollSkinImage,
    DollDrop,
    DollSDImage,
    DollEffect,
    DollEffectGrid,
    DollSkill,
)

admin.site.register(Doll)
admin.site.register(DollSkinImage)
admin.site.register(DollSDImage)
admin.site.register(DollDrop)
admin.site.register(DollEffect)
admin.site.register(DollEffectGrid)
admin.site.register(DollSkill)
