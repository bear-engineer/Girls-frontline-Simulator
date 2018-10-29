from django.conf import settings
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from doll.models import Doll
from doll.serializer import DollListSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DollList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    queryset = Doll.objects.all().order_by('id')
    serializer_class = DollListSerializer
    # def get(self, request, *args, **kwargs):
    #     result = []
    #     queryset = Doll.objects.values('id', 'code_name', 'rank', 'type', 'image').order_by('id')
    #     for item in queryset:
    #         item['image'] = settings.MEDIA_URL + item['image']
    #         result.append(item)
    #     pagination_class = StandardResultsSetPagination
    #     return Response(result)
