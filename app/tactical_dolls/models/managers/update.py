import requests
from django.db.models import Manager

__all__ = (
    'Update',
)


class Update(Manager):

    def update_doll(self):
        from tactical_dolls.models import Doll

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
                skill02_data = list(source['skill2']['dataPool'])
            except KeyError:
                skill01_consumption = None
                skill02_id = None
                skill02_codename = None
                skill02_cooldowntype = None
                skill02_initialcooldown = None
                skill02_consumption = None
                skill02_data = []

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
                'obtain': source.get('obtain'),
                'is_upgrade': is_upgrade,
            }

            doll, doll_create = Doll.objects.update_or_create(
                id=source.get('id'),
                defaults=doll_data,
            )

            doll_status = source['stats']
            doll.doll_status.update_or_create(
                hp=doll_status.get('hp'),
                pow=doll_status.get('pow'),
                hit=doll_status.get('hit'),
                dodge=doll_status.get('dodge'),
                speed=doll_status.get('speed'),
                rate=doll_status.get('rate'),
                armorpiercing=doll_status.get('armorPiercing'),
                criticalpercent=doll_status.get('criticalPercent'),
                bullet=doll_status.get('bullet'),
            )

            doll.doll_skill_data01.update_or_create(
                skill_id=source['skill1'].get('id'),
                codename=source['skill1'].get('codename'),
                cooldowntype=source['skill1'].get('cooldownType'),
                skill_data=list(source['skill1'].get('dataPool')),
                initialcooldown=source['skill1'].get('initialCooldown'),
                consumption=skill01_consumption,
            )

            doll.doll_skill_data02.update_or_create(
                skill_id=skill02_id,
                codename=skill02_codename,
                cooldowntype=skill02_cooldowntype,
                skill_data=skill02_data,
                initialcooldown=skill02_initialcooldown,
                consumption=skill02_consumption,

            )
            # for skill in source['skill1'].get('dataPool'):
            #     doll.doll_skill_data01.update_or_create(level=skill['level'], cooldown=skill['cooldown'])
            #
            # try:
            #     for skill in source['skill2'].get('dataPool'):
            #         doll.doll_skill_data02.update_or_create(level=skill['level'], cooldown=skill['cooldown'])
            # except KeyError:
            #     doll.doll_skill_data02.update_or_create(level=None, cooldown=None)

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
