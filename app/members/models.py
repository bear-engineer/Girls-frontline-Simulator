from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default User models
    """
    display_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='members_profile', blank=True)
    is_facebook = models.BooleanField(default=False, blank=True)
    is_kakao = models.BooleanField(default=False, blank=True)
    created_at = models.DateField(auto_now_add=True)
