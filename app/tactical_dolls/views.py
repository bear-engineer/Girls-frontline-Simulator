import requests
from django.http import HttpResponse
from django.views import View

from tactical_dolls.models import Doll


class Update(View):
    def get(request, *args, **kwargs):

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
                range = source['stats']['range']
            except KeyError:
                range = 0

            try:
                shield = source['stats']['shield']
            except KeyError:
                shield = 0

            try:
                critdmg = source['stats']['critDmg']
            except KeyError:
                critdmg = 0

            try:
                bullet = source['stats']['bullet']
            except KeyError:
                bullet = 0
            try:
                build_time = source['buildTime']
            except KeyError:
                build_time = 0

            try:
                illustrator_creator = source['illust']
            except KeyError:
                illustrator_creator = None

            try:
                voice = source['voice']
            except KeyError:
                voice = None

            try:
                krname = source['krName']
            except KeyError:
                krname = None
            try:
                night_view = source['night_view']
            except KeyError:
                night_view = 0
            try:
                cool_down = source['cool_down']
            except KeyError:
                cool_down = 0

            doll_data = {
                'kr_name': krname,
                'doll_id': source['id'],
                'build_time': build_time,
                'rank': source['rank'],
                'type': source['type'].upper(),
                'illust': illustrator_creator,
                'voice': voice,
            }

            doll_status_data = {
                'hp': source['stats']['hp'],
                'dodge': source['stats']['dodge'],
                'pow': source['stats']['pow'],
                'hit': source['stats']['hit'],
                'speed': source['stats']['speed'],
                'rate': source['stats']['rate'],
                'armor_piercing': armor_piercing,
                'crit': source['stats']['crit'],
                'armor': armor,
                'range': range,
                'shield': shield,
                'bullet': bullet,
                'critdmg': critdmg,
                'night_view': night_view,
                'cool_down': cool_down,
            }

            doll, doll_create = Doll.objects.update_or_create(
                name=source['name'],
                defaults=doll_data,
            )

            doll.doll_status.update_or_create(
                hp=source['stats']['hp'],
                defaults=doll_status_data,
            )
            doll.save()
            print(f"{source['name']} 저장 성공")

        return HttpResponse('update')
