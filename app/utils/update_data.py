import os
import requests


# from django.core.files.base import ContentFile


class DollUpdate:
    def __init__(self):
        self.data = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()

    def update(self):
        data = [item for item in self.data]

        def none_zero(value):
            if not value:
                value = 0
                return value
            return value

        def skill_value_data(key, value):
            item = key[value]
            skill_data = {
                'data': {
                    'id': item['id'],
                    'code_name': item['codename'],
                    'cool_down_type': item['cooldownType'],
                    'initial_cool_down': item['initialCooldown'],
                    'consumption': item['consumption']
                },
                'data_pool': item['dataPool']
            }
            return skill_data

        for item in data:
            default_data = {
                'id': item['id'],
                'code_name': item['codename'],
                'type': item['type'].upper(),
                'rank': item['rank'],
                'grow': item['grow'],
                'build_time': item['buildTime'],
                'obtain': item['obtain'],
                'slot_01': item['equip1'],
                'slot_02': item['equip2'],
                'slot_03': item['equip3'],
            }
            status_data = {
                'hp': item['stats']['hp'],
                'pow': item['stats']['pow'],
                'hit': item['stats']['hit'],
                'dodge': item['stats']['dodge'],
                'rate': item['stats']['rate'],
                'armor_piercing': item['stats']['armorPiercing'],
                'critical_harm_rate': none_zero(item['stats'].get('criticalHarmRate')),
                'critical_percent': none_zero(item['stats']['criticalPercent']),
                'bullet': none_zero(item['stats'].get('bullet')),
                'speed': none_zero(item['stats'].get('speed')),
                'night_view': none_zero(item['stats'].get('nightView')),
                'armor': none_zero(item['stats'].get('armor')),
            }
            effect_data = {
                'type': item['effect']['effectType'].upper(),
                'center': item['effect']['effectCenter'],
                'pos': item['effect']['effectPos'],
            }

            effect_grid_data = {
                'pow': none_zero(item['effect']['gridEffect'].get('pow')),
                'hit': none_zero(item['effect']['gridEffect'].get('hit')),
                'rate': none_zero(item['effect']['gridEffect'].get('rate')),
                'dodge': none_zero(item['effect']['gridEffect'].get('dodge')),
                'critical_percent': none_zero(item['effect']['gridEffect'].get('critical_percent')),
                'cool_down': none_zero(item['effect']['gridEffect'].get('cool_down')),
                'armor': none_zero(item['effect']['gridEffect'].get('armor')),
            }
            skill01_data = skill_value_data(item, 'skill1')
            if not item.get('skill2'):
                pass
            else:
                skill02_data = skill_value_data(item, 'skill2')


if __name__ == '__main__':
    DollUpdate().update()
