import requests
from django.http import HttpResponse
from django.views import View
import pprint

from tactical_dolls.models import Dolls


class Update(View):
    def get(self, request):
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()
        for index, source in enumerate(data_source):
            try:
                build_time = source['buildTime']
            except KeyError:
                build_time = 0

            try:
                armor_piercing = source['stats']['armorpiercing']
            except KeyError:
                armor_piercing = 0

            dolls_data = {
                'doll_no': source['id'],
                'doll_manufacturing_time': build_time,
                'doll_name': source['name'],
                'doll_range': source['rank'],
                'doll_type': source['type'],
                'doll_illustrator_creator': source['illust'],
                'doll_cv': source['voice'],
                'doll_hp': source['stats']['hp'],
                'doll_eva': source['stats']['dodge'],
                'doll_fp': source['stats']['pow'],
                'doll_acc': source['stats']['hit'],
                'doll_speed': source['stats']['speed'],
                'doll_rate': source['stats']['rate'],
                'doll_armorpiercing': source['stats']['armorpiercing'],
                'doll_crit': source['stats']['crit'],
                'doll_armor': source['']
            }
            dolls, dolls_create = Dolls.objects.update_or_create(
                defaults=dolls_data,
            )
            try:
                source['buildTime']
            except:
                print('build no', source['name'])
        return HttpResponse(data_source, content_type='application/json')
