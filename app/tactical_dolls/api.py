import json

from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from rest_framework.response import Response
from rest_framework.views import APIView
from utils.formula import Formula
# from utils.formula import EffectFormula as Formula
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
# @csrf_exempt
# def postman(request):
#     data = JSONParser().parse(request)
#     response = JSONRenderer().render(Formula(data).status_equip_effect_formula())
#
#     return HttpResponse(response, content_type='application/json')
#
#
# class TestView(APIView):
#     def get(self, request, *args, **kwargs):
#         print(request.data)
#         return Response(request.data)
#
#     def post(self, request, *args, **kwargs):
#         data = JSONRenderer().render(request.data)
#         print(data)
#         return Response(request.data)
