import requests
from django.http import HttpResponse
from django.views import View

from tactical_dolls.models import Doll


class Update(View):
    def get(self, request):
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()

        for source in data_source:
            try:
                armor_piercing = source['stats']['armorPiercing']

            except KeyError:
                armor_piercing = 0

            try:
                armor = source['stats']['armor']
            except KeyError:
                armor = 0

            try:
                doll_range = source['stats']['range']
            except KeyError:
                doll_range = 0

            try:
                doll_shield = source['stats']['shield']
            except KeyError:
                doll_shield = 0

            try:
                doll_critdmg = source['stats']['critDmg']
            except KeyError:
                doll_critdmg = 0

            try:
                doll_bullet = source['stats']['bullet']
            except KeyError:
                doll_bullet = 0
            try:
                build_time = source['buildTime']
            except KeyError:
                build_time = 0

            try:
                doll_illustrator_creator = source['illust']
            except KeyError:
                doll_illustrator_creator = None

            try:
                doll_cv = source['voice']
            except KeyError:
                doll_cv = None

            try:
                doll_krname = source['krName']
            except KeyError:
                doll_krname = None
            try:
                doll_nightview = source['doll_nightview']
            except KeyError:
                doll_nightview = 0
            try:
                doll_cooldown = source['doll_cooldown']
            except KeyError:
                doll_cooldown = 0

            dolls_data = {
                'doll_krname': doll_krname,
                'doll_no': source['id'],
                'doll_manufacturing_time': build_time,
                'doll_rating': source['rank'],
                'doll_type': source['type'].upper(),
                'doll_illustrator_creator': doll_illustrator_creator,
                'doll_cv': doll_cv,
                'doll_hp': source['stats']['hp'],
                'doll_eva': source['stats']['dodge'],
                'doll_fp': source['stats']['pow'],
                'doll_acc': source['stats']['hit'],
                'doll_speed': source['stats']['speed'],
                'doll_rate': source['stats']['rate'],
                'doll_armorpiercing': armor_piercing,
                'doll_crit': source['stats']['crit'],
                'doll_armor': armor,
                'doll_range': doll_range,
                'doll_shield': doll_shield,
                'doll_bullet': doll_bullet,
                'doll_critdmg': doll_critdmg,
                'doll_nightview': doll_nightview,
                'doll_cooldown': doll_cooldown,
            }
            dolls, dolls_create = Doll.objects.update_or_create(
                doll_name=source['name'],
                defaults=dolls_data,
            )

            dolls.save()
            print(f"{source['name']} 저장 성공")

        return HttpResponse(data_source, content_type='application/json')
