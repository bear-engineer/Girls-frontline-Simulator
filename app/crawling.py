import os

import requests
from django.core.files.base import ContentFile
from selenium import webdriver
from bs4 import BeautifulSoup
import django

# 장고 모듈 import
from tactical_dolls.models import Doll

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
driver = webdriver.Chrome('utils/webdriver/chromedriver')


class Crawling:
    """
    36base 데이터 크롤링
    """

    def __init__(self, source_url='http://localhost:3000'):
        self.source_url = source_url
        self.doll_id_list = []
        self.github_image_base_url = 'https://github.com/36base/girlsfrontline-resources/blob/master/pic/pic_'

    @property
    def doll_list_add(self):
        """
        doll id 값 파싱
        :return:
        """
        driver.get(self.source_url + '/doll')
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        doll_id = soup.select('div > a')

        for item in doll_id:
            self.doll_id_list.append(item.get('href'))
        return self.doll_id_list

    def create_doll(self):
        """
        36base, data json 동시 순회 및 DB create or update
        :return:
        """
        site_source = self.doll_list_add
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()

        for s_source, d_source in zip(site_source, data_source):
            driver.get(self.source_url + s_source)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            source_root = soup.select_one('main#content')

            # 컨텍스트 리스트
            context_list = [i.get_text(strip=True) for i in source_root.select('div > p')][1:]
            # 개조된 인형
            if 'Mod' in d_source.get('codename'):
                is_upgrade = True
            else:
                is_upgrade = False

            # 이벤트 전술인형 rank 예외처리
            if d_source.get('rank') == 7:
                rank = 'extra'.upper()
            else:
                rank = d_source.get('rank')

            # 전술 인형 기초정보
            doll_data = {
                'id': d_source.get('id'),
                'rank': rank,
                'type': d_source.get('type').upper(),
                'build_time': d_source.get('buildTime'),
                'codename': d_source.get('codename'),
                'kr_name': soup.select_one('div > div > h1').get_text(strip=True),
                'grow': d_source.get('grow'),
                'is_upgrade': is_upgrade,
            }

            # 전술 인형 기초 진형버프 정보
            doll_effect = {
                'type': d_source['effect'].get('effectType'),
                'center': d_source['effect'].get('effectCenter'),
            }

            # doll_status None 값 예외처리
            doll_status_bullet = d_source['stats'].get('bullet')
            if doll_status_bullet is None:
                doll_status_bullet = 0

            doll_status_armor = d_source['stats'].get('armor')
            if doll_status_armor is None:
                doll_status_armor = 0

            # 전술 인형 스테이터스
            doll_status = {
                'hp': int(context_list[8]),
                'pow': int(context_list[10]),
                'hit': int(context_list[12]),
                'dodge': int(context_list[14]),
                'speed': d_source['stats'].get('speed'),
                'rate': int(context_list[16]),
                'armor_piercing': d_source['stats'].get('armorPiercing'),
                'critical_percent': d_source['stats'].get('criticalPercent'),
                'bullet': doll_status_bullet,
                'armor': doll_status_armor,
            }

            # 전술 인형 기본 스킬 정보
            doll_skill01 = {
                'skill_id': d_source['skill1'].get('id'),
                'codename': d_source['skill1'].get('codename'),
                'cool_down_type': d_source['skill1'].get('cooldownType'),
                'initial_cool_down': d_source['skill1'].get('initialCooldown'),
                'consumption': d_source['skill1'].get('consumption'),
            }

            # 전술 인형 Upgrade 스킬 정보
            try:
                doll_skill02 = {
                    'skill_id': d_source['skill2'].get('id'),
                    'codename': d_source['skill2'].get('codename'),
                    'cool_down_type': d_source['skill2'].get('cooldownType'),
                    'initial_cool_down': d_source['skill2'].get('initialCooldown'),
                    'consumption': d_source['skill2'].get('consumption'),
                }
            except KeyError:
                doll_skill02 = {
                    'skill_id': None,
                    'codename': None,
                    'cool_down_type': None,
                    'initial_cool_down': None,
                    'consumption': None,
                }

            # base doll create
            doll, doll_create = Doll.objects.update_or_create(
                defaults=doll_data
            )
            doll_image = f'{self.github_image_base_url}{d_source.get("codename")}.png?raw=true'
            doll_image_d = f'{self.github_image_base_url}{d_source.get("codename")}_D.png?raw=true'
            doll.image.save(
                doll_image, ContentFile(requests.get(doll_image).content)
            )
            doll.image_d.save(
                doll_image_d, ContentFile(requests.get(doll_image_d).content)
            )

            # doll status
            doll.doll_status.update_or_create(
                defaults=doll_status
            )

            doll.doll_skill01.update_or_create(
                defaults=doll_skill01
            )

            for data in d_source['skill1'].get('dataPool'):
                doll.doll_skill01_data.update_or_create(
                    level=data.get('level'),
                    cool_down=data.get('colldown'),
                )
            doll.doll_skill02.update_or_create(
                defaults=doll_skill02
            )

            try:
                skill02_source = d_source['skill2'].get('dataPool')
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

            for data in d_source['effect'].get('effectPos'):
                doll.doll_effect_pos.update_or_create(
                    pos=data,
                )

            effect_grid = d_source['effect'].get('gridEffect')
            doll.doll_effect_grid.update_or_create(
                pow=effect_grid.get('pow'),
                hit=effect_grid.get('hit'),
                rate=effect_grid.get('rate'),
                dodge=effect_grid.get('dodge'),
                critical_percent=effect_grid.get('criticalPercent'),
                cool_down=effect_grid.get('cooldown'),
                armor=effect_grid.get('armor'),
            )
            for data in d_source['equip1']:
                doll.doll_equip_slot01.update_or_create(
                    module=data,
                )

            for data in d_source['equip2']:
                doll.doll_equip_slot02.update_or_create(
                    module=data,
                )

            for data in d_source['equip3']:
                doll.doll_equip_slot03.update_or_create(
                    module=data,
                )

            try:
                mind_update_source = d_source['mindupdate']
            except KeyError:
                mind_update_source = []

            for data in mind_update_source:
                doll.doll_mind_update.update_or_create(
                    core=data.get('core'),
                    mind_piece=data.get('mempiece')
                )
            if doll_create is True:
                print(f'{d_source.get("codename")} 생성 완료')
            else:
                print(f'{d_source.get("codename")} 업데이트 완료')
            doll.save()


if __name__ == '__main__':
    Crawling().create_doll()
