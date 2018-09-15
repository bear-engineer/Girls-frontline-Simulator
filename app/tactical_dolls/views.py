import requests
from django.http import HttpResponse
from django.views import View

from tactical_dolls.models import Doll


class Update(View):
    """
    인형 정보를 업데이트 합니다.
    """

    def get(request, *args, **kwargs):

        # 인형 데이터 Json source
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()

        # 모든 데이터를 순차적으로 DB에 저장
        for source in data_source:

            if 'Mod' in source['name']:
                is_upgrade = True
            else:
                is_upgrade = False

            # info
            # illust = source.get('illust')
            # voice = source.get('voice')
            # krName = source.get('krName')
            # buildTime = source.get('buildTime')

            # drop
            drop_field = source.get('drop')

            # effect
            effect_type = source['effect'].get('effectType')
            effect_center = source['effect'].get('effectCenter')
            effect_pos = source['effect'].get('effectPos')

            # status
            armor_piercing = source['stats'].get('armorPiercing')
            armor = source['stats'].get('armor')
            range = source['stats'].get('range')
            shield = source['stats'].get('shield')
            critdmg = source['stats'].get('critDmg')
            bullet = source['stats'].get('bullet')
            night_view = source['stats'].get('night_view')
            cool_down = source['stats'].get('cool_down')

            doll_data = {
                'kr_name': source.get('krName'),
                'doll_id': source['id'],
                'build_time': source.get('buildTime'),
                'rank': source['rank'],
                'type': source['type'].upper(),
                'illust': source.get('illust'),
                'voice': source.get('voice'),
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
            doll_effect_data = {
                'effect_type': effect_type.upper(),
                'effect_center': effect_center,
                'effect_pos': effect_pos,
            }

            doll, doll_create = Doll.objects.update_or_create(
                name=source['name'],
                defaults=doll_data,
            )

            doll.doll_status.update_or_create(
                # hp=source['stats']['hp'],
                defaults=doll_status_data,
            )

            doll.doll_effect.update_or_create(
                # effect_center=effect_type,
                defaults=doll_effect_data,
            )

            # 해당하는 필드가 없는 경우 None
            doll.doll_drop.update_or_create(
                drop_field=drop_field,
            )
            doll.save()
            print(f"{source['name']} 저장 성공")

        return HttpResponse('update')
