from rest_framework import generics
from rest_framework.views import APIView

from .serializer import DollSerializer, DollDetailSerializer
from .models import Doll


class Dolls(generics.ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollSerializer


class DollDetail(generics.RetrieveAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollDetailSerializer


class EffectFormula(APIView):
    def post(self, request, *args, **kwargs):
        source = request.data
        return self.get(request, *args, **kwargs)
