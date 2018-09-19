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

            doll.doll_effect.update_or_create(
                effecttype=source['effect']['effectType'],
                effectcenter=source['effect']['effectCenter'],
                effectpos=source['effect']['effectPos'],
            )
            grideffect = source['effect']['gridEffect']
            doll.doll_effect_grid.update_or_create(
                pow=grideffect.get('pow'),
                hit=grideffect.get('hit'),
                rate=grideffect.get('rate'),
                dodge=grideffect.get('dodge'),
                criticalpercent=grideffect.get('criticalPercent'),
                cooldown=grideffect.get('cooldown'),
                armor=grideffect.get('armor'),
            )

            doll.save()
            print(f"{source['codename']} 저장 성공")

        return HttpResponse('update')
