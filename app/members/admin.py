from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('ID/Password', {
            'fields': (
                'username',
                'password',
            ),
        }),
        ('닉네임',{
            'fields':(
                'display_name',
            ),
        }),
        ('이메일', {
            'fields': (
                'email',
            ),
        }),
        ('계정 유형', {
            'fields': (
                'is_facebook',
                'is_kakao',
            ),
        }),
        ('권한', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
        ('프로필 이미지', {
            'fields': (
                'profile_image',
            ),
        }),
    )


admin.site.register(User, UserAdmin)
