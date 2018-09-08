from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default User models
    """
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='members_profile')
    is_facebook = models.BooleanField(default=False, blank=True)
    is_kakao = models.BooleanField(default=False, blank=True)
