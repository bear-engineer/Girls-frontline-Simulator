import json

from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from utils.formula import EffectFormula as Formula
from .serializer import DollSerializer, DollDetailSerializer
from .models import Doll


class Dolls(generics.ListAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollSerializer


class DollDetail(generics.RetrieveAPIView):
    queryset = Doll.objects.all()
    serializer_class = DollDetailSerializer


@csrf_exempt
def postman(request):
    data = JSONParser().parse(request)
    response = JSONRenderer().render(Formula(data).status_equip_effect_formula())

    return HttpResponse(response, content_type='application/json')
