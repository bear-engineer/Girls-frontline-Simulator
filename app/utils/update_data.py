import os
import requests


# from django.core.files.base import ContentFile


class DollUpdate:
    def __init__(self):
        self.base_url = 'https://raw.githubusercontent.com/36base/'
        self.data = requests.get(f'{self.base_url}girlsfrontline-core/master/data/doll.json').json()
        self.image_data = 'https://github.com/36base/girlsfrontline-resources/blob/master/pic/pic_'
        self.skill_image_data = f'{self.base_url}girlsfrontline-resources/master/icon/skillicon/'
        self.voice_data = requests.get(
            f'{self.base_url}girlsfrontline-extra-data/master/data/locale/ko-KR/NewCharacterVoice.json'
        ).json()

    def update(self):

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

        for item in self.data:
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

            image = f'{self.image_data}{item.get("codename").lower()}.png?raw=true'
            image_d = f'{self.image_data}{item.get("codename").lower()}_D.png?raw=true'

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

            voice_item = self.voice_data.get(item['codename'])
            if not voice_item:
                pass
            else:
                voice_data = {
                    'doll': '',
                    'dialogue01': voice_item.get('dialogue1'),
                    'dialogue02': voice_item.get('dialogue2'),
                    'dialogue03': voice_item.get('dialogue3'),
                    'introduce': voice_item.get('introduce'),
                    'allhallows': voice_item.get('allhallows'),
                    'soul_contract': voice_item.get('soulcontract'),
                    'dialogue_wedding': voice_item.get('dialoguewedding'),
                    'gain': voice_item.get('gain'),
                }

            skill01_data = skill_value_data(item, 'skill1')
            skill01_image = f'{self.skill_image_data}{skill01_data["data"]["code_name"].lower()}.png?raw=true'
            if not item.get('skill2'):
                pass
            else:
                skill02_data = skill_value_data(item, 'skill2')

            # print(default_data)
            # Voice.objects.get(code_name=item_voice)


if __name__ == '__main__':
    DollUpdate().update()
