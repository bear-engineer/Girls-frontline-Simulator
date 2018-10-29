from django.db.models import Q
from django.test import TestCase

from doll.models import Doll
from equip.models import Equip


class Testclasss(TestCase):
    def test(self):
        with self.assertNumQueries(1):
            # print(Doll.objects.all())
            # print(Equip.objects.all())
            # for i in range(3):
            print(Doll.objects.filter(Q(id=1) | Q(id=2) | Q(id=3)).prefetch_related(
                'effect_set__effectgrid_set',
                'voice_set',
                'skill_set__skilldata_set',
            ).values('effect__effectgrid__pow'))


if __name__ == '__main__':
    Testclasss().test()
