from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from doll.models import Doll
from doll.serializer import DollListSerializer
from utils.simulator import Simulator


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DollList(generics.ListAPIView):
    pagination_class = StandardResultsSetPagination
    queryset = Doll.objects.all().order_by('id')
    serializer_class = DollListSerializer


class SimulatorView(APIView):
    def get(self, request, *args, **kwargs):
        # query_set = Doll.objects.all().values(
        #     'id',
        #     'code_name',
        #     'image',
        #     'rank',
        #     'type',
        # )
        data = [
            {
                "id": 1,
                "position": 5,
                "slot_01": None,
                "slot_02": None,
                "slot_03": None,
            },
            {
                "id": 1002,
                "position": 3,
                "slot_01": 61,
                "slot_02": None,
                "slot_03": None,
            },
            {
                "id": 2,
                "position": 3,
                "slot_01": None,
                "slot_02": None,
                "slot_03": None,
            },
            {
                "id": 3,
                "position": 7,
                "slot_01": None,
                "slot_02": None,
                "slot_03": None,
            },
            {
                "id": 4,
                "position": 1,
                "slot_01": None,
                "slot_02": None,
                "slot_03": None,
            }
        ]
        print(request.GET)
        return Response(Simulator(data).position_result)

    def post(self, request, *args, **kwargs):
        return Response(Simulator(request).test_return)
