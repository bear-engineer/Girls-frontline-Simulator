from django.contrib import admin

# Register your models here.
from .models import (
    Doll,
    DollSkinImage,
    DollDrop,

    DollEffect,
    DollEffectGrid,
    DollSkill01,
    DollSkill02,
)

admin.site.register(Doll)
admin.site.register(DollSkinImage)
admin.site.register(DollDrop)
admin.site.register(DollEffect)
admin.site.register(DollEffectGrid)
admin.site.register(DollSkill01)
admin.site.register(DollSkill02)
