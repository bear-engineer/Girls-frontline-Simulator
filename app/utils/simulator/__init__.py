from django.utils.functional import cached_property

from .status import Status
from .position import Positions
from .equip import EquipCalculation
from doll.models import Doll
from equip.models import Equip

import django

django.setup()


class Simulator:

    def __init__(self, data):
        self.data = data
        self.doll_data = Doll.objects.filter(id__in=[item['id'] for item in self.data]).prefetch_related(
            'effect_set', 'effect_set__effectgrid_set', 'status_set'
        ).values(
            'id',
            'code_name',
            'image',
            'rank',
            'type',
            'slot_01',
            'slot_02',
            'slot_03',
            'grow',
            'status__hp',
            'status__pow',
            'status__hit',
            'status__dodge',
            'status__rate',
            'status__armor',
            'status__critical_harm_rate',
            'status__critical_percent',
            'status__bullet',
            'status__speed',
            'status__night_view',
            'status__armor',
            'effect__type',
            'effect__center',
            'effect__pos',
            'effect__effectgrid__pow',
            'effect__effectgrid__hit',
            'effect__effectgrid__rate',
            'effect__effectgrid__dodge',
            'effect__effectgrid__critical_percent',
            'effect__effectgrid__cool_down',
            'effect__effectgrid__armor',
        )
        self.result = []

    @cached_property
    def equip_query_set(self):
        query_data = []
        query_data_set = {}
        result = {}
        for item in self.data:
            for value in [item['slot_01'], item['slot_02'], item['slot_03']]:
                if not value:
                    continue
                query_data.append(value)
        query = Equip.objects.filter(id__in=query_data).values()

        for item in query:
            query_data_set[item['id']] = item
        for item in self.data:
            for item_name in 'slot_01,slot_02,slot_03'.split(','):
                if not item[item_name]:
                    continue
                item[item_name] = query_data_set[item[item_name]]
        for item in self.data:
            result[item['id']] = item
        return result

    @cached_property
    def status_result(self):
        return Status(self.doll_data).formula

    @cached_property
    def position_result(self):
        return Positions(self.doll_query_set).position_effect_calculation()

    @cached_property
    def equip_result(self):
        return EquipCalculation(self.status_result, self.equip_query_set).equip_calculation()

    @cached_property
    def doll_query_set(self):
        data_set = []
        request_data_set = {}
        for data in self.data:
            request_data_set[data['id']] = data['position']

        for index, item in enumerate(self.equip_result):
            data = {
                'position': request_data_set[item['id']],
                'position_xy': [],
                'id': item['id'],
                'doll_info': item,
                'effect_info': {},
            }
            data_set.append(data)
        return data_set
