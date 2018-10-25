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
        # test data
        da = [{"id": 93, "center": 2, "slot_01": 102, "slot_02": None, "slot_03": None},
              {"id": 2, "center": 1, "slot_01": None, "slot_02": None, "slot_03": None}]
        result = Formula(da).formula_result
        return Response(result)
