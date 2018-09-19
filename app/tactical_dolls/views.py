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

            try:
                skill01_consumption = source['skill1']['consumption']
                skill02_id = source['skill2'].get('id')
                skill02_codename = source['skill2'].get('codename')
                skill02_cooldowntype = source['skill2'].get('cooldownType')
                skill02_initialcooldown = source['skill2'].get('initialCooldown')
                skill02_consumption = source['skill2']['consumption']
            except KeyError:
                skill01_consumption = None
                skill02_id = None
                skill02_codename = None
                skill02_cooldowntype = None
                skill02_initialcooldown = None
                skill02_consumption = None

            doll_data = {
                'id': source.get('id'),
                'rank': source.get('rank'),
                'type': source.get('type'),
                'buildtime': source.get('buildTime'),
                'codename': source.get('codename'),
                'grow': source.get('grow'),
                'equip01': source.get('equip1'),
                'equip02': source.get('equip2'),
                'equip03': source.get('equip3'),
                'mindupdata': source.get('mindupdate'),
                'skill01_id': source['skill1'].get('id'),
                'skill01_codename': source['skill1'].get('codename'),
                'skill01_cooldowntype': source['skill1'].get('cooldownType'),
                'skill01_initialcooldown': source['skill1'].get('initialCooldown'),
                'skill01_consumption': skill01_consumption,
                'skill02_id': skill02_id,
                'skill02_codename': skill02_codename,
                'skill02_cooldowntype': skill02_cooldowntype,
                'skill02_initialcooldown': skill02_initialcooldown,
                'skill02_consumption': skill02_consumption,
                'obtain': source.get('obtain'),
                'is_upgrade': is_upgrade,
            }

            # doll_data = {
            #     'kr_name': source.get('krName'),
            #     'doll_id': source['id'],
            #     'build_time': source.get('buildTime'),
            #     'rank': source['rank'],
            #     'type': source['type'].upper(),
            #     'illust': source.get('illust'),
            #     'voice': source.get('voice'),
            #     'is_upgrade': is_upgrade,
            # }

            # doll_status_data = {
            #     'hp': source['stats']['hp'],
            #     'dodge': source['stats']['dodge'],
            #     'pow': source['stats']['pow'],
            #     'hit': source['stats']['hit'],
            #     'speed': source['stats']['speed'],
            #     'rate': source['stats']['rate'],
            #     'armor_piercing': source['stats'].get('armorPiercing'),
            #     'crit': source['stats']['criticalPercent'],
            #     'armor': source['stats'].get('armorPiercing'),
            #     'range': source['stats'].get('range'),
            #     'shield': source['stats'].get('shield'),
            #     'bullet': source['stats'].get('bullet'),
            #     'critdmg': source['stats'].get('critDmg'),
            #     'night_view': source['stats'].get('night_view'),
            #     'cool_down': source['stats'].get('cool_down'),
            # }
            # doll_effect_data = {
            #     'effect_type': source['effect'].get('effectType').upper(),
            #     'effect_center': source['effect'].get('effectCenter'),
            #     'effect_pos': source['effect'].get('effectPos'),
            # }

            doll, doll_create = Doll.objects.update_or_create(
                id=source.get('id'),
                defaults=doll_data,
            )

            for skill in source['skill1'].get('dataPool'):
                doll.doll_skill_data01.update_or_create(level=skill['level'], cooldown=skill['cooldown'])

            try:
                for skill in source['skill2'].get('dataPool'):
                    doll.doll_skill_data02.update_or_create(level=skill['level'], cooldown=skill['cooldown'])
            except KeyError:
                doll.doll_skill_data02.update_or_create(level=None, cooldown=None)
            # doll.doll_status.update_or_create(
            #     # hp=source['stats']['hp'],
            #     defaults=doll_status_data,
            # )
            #
            # doll.doll_effect.update_or_create(
            #     # effect_center=effect_type,
            #     defaults=doll_effect_data,
            # )

            # doll.doll_drop.update_or_create(
            #     drop_field=source.get('drop'),
            # )
            doll.save()
            print(f"{source['codename']} 저장 성공")

        return HttpResponse('update')
