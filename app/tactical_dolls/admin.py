from django.contrib import admin

# Register your models here.
from .models import Dolls, DollsSkinImage, DollsDrop, DollsSDImage

admin.site.register(Dolls)
admin.site.register(DollsSkinImage)
admin.site.register(DollsSDImage)
admin.site.register(DollsDrop)
