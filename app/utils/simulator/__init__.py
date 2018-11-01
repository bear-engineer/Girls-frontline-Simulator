from django.utils.functional import cached_property
import math
from doll.models import Doll
from equip.models import Equip


class Status:
    def __init__(self, query):
        self.query = query
        self.grow_data = {
            "after100": {
                "basic": {
                    "armor": [13.979, 0.04],
                    "hp": [96.283, 0.138]
                },
                "grow": {
                    "dodge": [0.075, 22.572],
                    "hit": [0.075, 22.572],
                    "pow": [0.06, 18.018],
                    "rate": [0.022, 15.741]
                }
            },
            "normal": {
                "basic": {
                    "armor": [2, 0.161],
                    "dodge": [5],
                    "hit": [5],
                    "hp": [55, 0.555],
                    "pow": [16],
                    "rate": [45],
                    "speed": [10]
                },
                "grow": {
                    "dodge": [0.303, 0],
                    "hit": [0.303, 0],
                    "pow": [0.242, 0],
                    "rate": [0.181, 0]
                }
            }
        }
        self.attr_data = {
            "hg": {
                "hp": 0.6,
                "pow": 0.6,
                "rate": 0.8,
                "speed": 1.5,
                "hit": 1.2,
                "dodge": 1.8
            },
            "smg": {
                "hp": 1.6,
                "pow": 0.6,
                "rate": 1.2,
                "speed": 1.2,
                "hit": 0.3,
                "dodge": 1.6
            },
            "rf": {
                "hp": 0.8,
                "pow": 2.4,
                "rate": 0.5,
                "speed": 0.7,
                "hit": 1.6,
                "dodge": 0.8
            },
            "ar": {
                "hp": 1,
                "pow": 1,
                "rate": 1,
                "speed": 1,
                "hit": 1,
                "dodge": 1
            },
            "mg": {
                "hp": 1.5,
                "pow": 1.8,
                "rate": 1.6,
                "speed": 0.4,
                "hit": 0.6,
                "dodge": 0.6
            },
            "sg": {
                "hp": 2.0,
                "pow": 0.7,
                "rate": 0.4,
                "speed": 0.6,
                "hit": 0.3,
                "dodge": 0.3,
                "armor": 1
            }
        }

    @cached_property
    def formula(self):
        level = 100
        favor = 100
        dummy = 5

        for item in self.query:

            status_list = 'hp,armor,hit,pow,dodge,rate'.split(',')
            doll_type = item['type'].lower()
            grow = item['grow']
            for stats in status_list:
                doll_status = float(item[f'status__{stats}'])
                if stats == 'hp' or stats == 'armor':
                    try:
                        attr_data = float(self.attr_data[doll_type][stats])
                    except KeyError:
                        continue
                    if level <= 100:
                        basic_data0 = float(self.grow_data['normal']['basic'][stats][0])
                        basic_data1 = float(self.grow_data['normal']['basic'][stats][1])
                        basic_formula = math.ceil(
                            (basic_data0 + ((level - 1) * basic_data1)) * attr_data * doll_status / 100
                        )
                        item[f'status__{stats}'] = basic_formula * dummy
                    else:
                        basic_data0 = float(self.grow_data['after100']['basic'][stats][0])
                        basic_data1 = float(self.grow_data['after100']['basic'][stats][1])
                        basic_formula = math.ceil(
                            (basic_data0 + ((level - 1) * basic_data1)) * attr_data * doll_status / 100
                        )
                        item[f'status__{stats}'] = basic_formula * dummy
                else:
                    attr_data = float(self.attr_data[doll_type][stats])

                    grow_data0 = float(self.grow_data['after100']['grow'][stats][0])
                    grow_data1 = float(self.grow_data['after100']['grow'][stats][1])

                    normal_basic = self.grow_data['normal']['basic'][stats]

                    normal_basic_formula = math.ceil(
                        normal_basic[0] * attr_data * doll_status / 100
                    )
                    normal_grow_formula = math.ceil(
                        (grow_data1 + ((level - 1) * grow_data0)) * attr_data * doll_status * grow / 100 / 100
                    )

                    item[f'status__{stats}'] = normal_basic_formula + normal_grow_formula

        return self.query


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
