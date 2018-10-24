from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.formula import Formula
from .serializer import DollSerializer, DollDetailSerializer
from .models import Doll


class Dolls(generics.ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollSerializer


class DollDetail(generics.RetrieveAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollDetailSerializer


class DollFormula(APIView):
    def post(self, request, *args, **kwargs):
        result = Formula(request.data).formula_result
        print(result)
        return Response(result)

    def get(self, request, *args, **kwargs):
        return Response('get')
