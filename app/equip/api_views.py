from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from equip.models import Equip
from equip.serializer import EquipListSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000


class EquipList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    queryset = Equip.objects.all().order_by('id')
    serializer_class = EquipListSerializer
