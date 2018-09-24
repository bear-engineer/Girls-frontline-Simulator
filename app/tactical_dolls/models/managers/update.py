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

            doll_basic_data = {
                'id': source.get('id'),
                'rank': source.get('rank'),
                'type': source.get('type'),
                'build_time': source.get('buildTime'),
                'codename': source.get('codename'),
                'grow': source.get('grow'),
                'is_upgrade': is_upgrade,
            }

            doll_effect = {
                'type': source['effect'].get('effectType'),
                'center': source['effect'].get('effectCenter'),
            }

            doll_status = {
                'hp': source['stats'].get('hp'),
                'pow': source['stats'].get('pow'),
                'hit': source['stats'].get('hit'),
                'dodge': source['stats'].get('dodge'),
                'speed': source['stats'].get('speed'),
                'rate': source['stats'].get('rate'),
                'armor_piercing': source['stats'].get('armorPiercing'),
                'critical_percent': source['stats'].get('criticalPercent'),
                'bullet': source['stats'].get('bullet'),
            }

            doll_skill01 = {
                'skill_id': source['skill1'].get('id'),
                'codename': source['skill1'].get('codename'),
                'cool_down_type': source['skill1'].get('cooldownType'),
                'initial_cool_down': source['skill1'].get('initialCooldown'),
                'consumption': source['skill1'].get('consumption'),
            }

            try:
                doll_skill02 = {
                    'skill_id': source['skill2'].get('id'),
                    'codename': source['skill2'].get('codename'),
                    'cool_down_type': source['skill2'].get('cooldownType'),
                    'initial_cool_down': source['skill2'].get('initialCooldown'),
                    'consumption': source['skill2'].get('consumption'),
                }
            except KeyError:
                doll_skill02 = {
                    'skill_id': None,
                    'codename': None,
                    'cool_down_type': None,
                    'initial_cool_down': None,
                    'consumption': None,
                }

            doll, doll_create = Doll.objects.update_or_create(
                id=source.get('id'),
                defaults=doll_basic_data,
            )

            doll.doll_status.update_or_create(
                defaults=doll_status,
            )

            doll.doll_skill01.update_or_create(
                defaults=doll_skill01
            )

            for data in source['skill1'].get('dataPool'):
                doll.doll_skill01_data.update_or_create(
                    level=data.get('level'),
                    cool_down=data.get('cooldown'),
                )

            doll.doll_skill02.update_or_create(
                defaults=doll_skill02
            )

            try:
                skill02_source = source['skill2'].get('dataPool')
            except KeyError:
                skill02_source = []

            for data in skill02_source:
                doll.doll_skill02_data.update_or_create(
                    level=data.get('level'),
                    cool_down=data.get('cooldown')
                )

            doll.doll_effect.update_or_create(
                defaults=doll_effect,
            )

            for data in source['effect'].get('effectPos'):
                doll.doll_effect_pos.update_or_create(
                    pos=data,
                )

            effect_grid = source['effect'].get('gridEffect')
            doll.doll_effect_grid.update_or_create(
                pow=effect_grid.get('pow'),
                hit=effect_grid.get('hit'),
                rate=effect_grid.get('rate'),
                dodge=effect_grid.get('dodge'),
                critical_percent=effect_grid.get('criticalPercent'),
                cool_down=effect_grid.get('cooldown'),
                armor=effect_grid.get('armor'),
            )

            doll.save()
            print(f"{source['codename']} 저장 성공")
