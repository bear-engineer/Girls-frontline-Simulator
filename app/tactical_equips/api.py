from rest_framework import generics

from tactical_equips.models import DollEquip
from .serializer import EquipSerializer


class DollsEquip(generics.ListAPIView):
    queryset = DollEquip.objects.all()
    serializer_class = EquipSerializer
