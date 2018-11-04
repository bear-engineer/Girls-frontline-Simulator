from django.utils.functional import cached_property
import math
from .status import Status
from doll.models import Doll
from equip.models import Equip


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
        result = []
        for item in self.data:
            for value in [item['slot_01'], item['slot_02'], item['slot_03']]:
                if not value:
                    continue
                result.append(value)
        return Equip.objects.filter(id__in=result).values()

    @cached_property
    def doll_query_set(self):
        data_set = []
        for index, item in enumerate(self.status_result):
            data = {
                'position': self.data[index]['position'],
                'position_xy': [],
                'id': self.data[index]['id'],
                'doll_info': item,
            }
            data_set.append(data)
        return data_set

    @cached_property
    def status_result(self):
        return Status(self.doll_data).formula


class Positions:
    def __init__(self, query):

        self.query_set = query
        self.relative_position = {
            1: (-1, 1),
            2: (0, 1),
            3: (1, 1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, -1),
            8: (0, -1),
            9: (1, -1),
        }
        self.result = []

    def get_position(self):
        for data in self.query_set:
            position_list = data['doll_info']['effect__pos']

            for item in position_list:
                data['position_xy'].append((
                    self.relative_position[data['position']][0] - self.relative_position[item][0],
                    self.relative_position[data['position']][1] - self.relative_position[item][1]
                ))
        return self.query_set
