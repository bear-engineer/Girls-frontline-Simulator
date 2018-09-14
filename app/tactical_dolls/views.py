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
                if source['illust'] == '':
                    illust = None
                else:
                    illust = source['illust']
            except KeyError:
                illust = None

            try:
                if source['voice'] == '':
                    voice = None
                else:
                    voice = source['voice']
            except KeyError:
                voice = None
            try:
                krname = source['krName']
            except KeyError:
                krname = None
            try:
                build_time = source['buildTime']
            except KeyError:
                build_time = 0
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
                night_view = source['night_view']
            except KeyError:
                night_view = 0
            try:
                cool_down = source['cool_down']
            except KeyError:
                cool_down = 0
            try:
                drop_field = source['drop']
            except KeyError:
                drop_field = None

            if 'Mod' in source['name']:
                is_upgrade = True
            else:
                is_upgrade = False

            doll_data = {
                'kr_name': krname,
                'doll_id': source['id'],
                'build_time': build_time,
                'rank': source['rank'],
                'type': source['type'].upper(),
                'illust': illust,
                'voice': voice,
                'is_upgrade': is_upgrade,
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

            # 해당하는 필드가 없는 경우 None
            try:
                for doll_drop_field in drop_field:
                    doll.doll_drop.update_or_create(
                        drop_field=doll_drop_field,
                    )
            except TypeError:
                doll.doll_drop.update_or_create(
                    drop_field=None,
                )
            doll.save()
            print(f"{source['name']} 저장 성공")

        return HttpResponse('update')
