from rest_framework import generics

from .serializer import DollSerializer, DollDetailSerializer
from .models import Doll


class Dolls(generics.ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollSerializer


class DollDetail(generics.RetrieveAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollDetailSerializer

