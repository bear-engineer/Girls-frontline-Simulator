from django.urls import path

from tactical_equips.api import DollsEquip

urlpatterns = [
    path('all/', DollsEquip.as_view()),
]
