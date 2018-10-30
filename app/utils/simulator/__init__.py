from django.utils.functional import cached_property

from doll.models import Doll
from equip.models import Equip


class Simulator:
    """
    Data values
    [
        {
            'id':1,
            'position':5,
            'slot_01':None,
            'slot_02':None,
            'slot_03':None,
        },
        {
            'id':2,
            'position':7,
            'slot_01':None,
            'slot_02':None,
            'slot_03':None,
        },
    ]
    """

    def __init__(self, data):
        self.data = data
        self.doll_query_set = Doll.objects.filter(id__in=[item['id'] for item in self.data]).prefetch_related(
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

    @property
    def test_return(self):
        return self.doll_query_set

    @cached_property
    def equip_query_set(self):
        result = []
        for item in self.data:
            for value in [item['slot_01'], item['slot_02'], item['slot_03']]:
                if not value:
                    continue
                result.append(value)
        return Equip.objects.filter(id__in=result).values()


class Positions:
    def __init__(self, **kwargs):
        self.position = kwargs['position']
        self.pow = kwargs['pow']
