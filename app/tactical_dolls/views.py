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

            # 개조된 인형을 구
            if 'Mod' in source.get('codename'):
                is_upgrade = True
            else:
                is_upgrade = False

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
                'armor_piercing': source['stats'].get('armorPiercing'),
                'crit': source['stats']['criticalPercent'],
                'armor': source['stats'].get('armorPiercing'),
                'range': source['stats'].get('range'),
                'shield': source['stats'].get('shield'),
                'bullet': source['stats'].get('bullet'),
                'critdmg': source['stats'].get('critDmg'),
                'night_view': source['stats'].get('night_view'),
                'cool_down': source['stats'].get('cool_down'),
            }
            doll_effect_data = {
                'effect_type': source['effect'].get('effectType').upper(),
                'effect_center': source['effect'].get('effectCenter'),
                'effect_pos': source['effect'].get('effectPos'),
            }

            doll, doll_create = Doll.objects.update_or_create(
                name=source.get('codename'),
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

            doll.doll_drop.update_or_create(
                drop_field=source.get('drop'),
            )
            doll.save()
            print(f"{source['codename']} 저장 성공")

        return HttpResponse('update')
