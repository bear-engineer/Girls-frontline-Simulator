import os
import requests
from django.core.files.base import ContentFile
from selenium import webdriver
from bs4 import BeautifulSoup
import django

# 장고 모듈 import


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()
from tactical_dolls.models import Doll, DollDetail
from tactical_equips.models import DollEquip


class Crawling:
    """
    36base 데이터 크롤링
    """

    def __init__(self, source_url='http://localhost:3000'):
        self.source_url = source_url
        self.doll_id_list = []
        self.equip_id_list = []
        self.github_image_base_doll_url = 'https://github.com/36base/girlsfrontline-resources/blob/master/pic/pic_'
        self.github_image_base_equip_url = 'https://github.com/36base/girlsfrontline-resources/blob/master/icon/equip/'
        self.driver = webdriver.Chrome('utils/webdriver/chromedriver')

    @property
    def doll_list_add(self):
        """
        doll id 값 파싱
        :return:
        """
        self.driver.get(self.source_url + '/doll')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        doll_id = soup.select('div > a')

        for item in doll_id:
            self.doll_id_list.append(item.get('href'))
        # self.driver.close()
        return self.doll_id_list

    @property
    def equip_list_add(self):
        """
        equip id 값 파싱
        :return:
        """
        source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/equip.json').json()
        for item in source:
            self.equip_id_list.append(f'/equip/{item.get("id")}')
        # self.driver.close()
        return self.equip_id_list

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
            self.driver.get(self.source_url + s_source)
            html = self.driver.page_source
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

            # equip data
            equip_slot_01 = ''
            for equip_type in d_source['equip1']:
                equip_slot_01 += f'{equip_type}'

            equip_slot_02 = ''
            for equip_type in d_source['equip2']:
                equip_slot_02 += f'{equip_type}'

            equip_slot_03 = ''
            for equip_type in d_source['equip3']:
                equip_slot_03 += f'{equip_type}'

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
                'equip_slot_01': equip_slot_01,
                'equip_slot_02': equip_slot_02,
                'equip_slot_03': equip_slot_03,
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
                codename=d_source.get('codename'),
                defaults=doll_data
            )
            doll_image = f'{self.github_image_base_doll_url}{d_source.get("codename")}.png?raw=true'
            doll_image_d = f'{self.github_image_base_doll_url}{d_source.get("codename")}_D.png?raw=true'
            doll.image.save(
                f'{d_source.get("codename")}.png', ContentFile(requests.get(doll_image).content)
            )
            doll.image_d.save(
                f'{d_source.get("codename")}_D.png', ContentFile(requests.get(doll_image_d).content)
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
                    cool_down=data.get('cooldown'),
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

            try:
                mind_update_source = d_source['mindupdate']
            except KeyError:
                mind_update_source = []

            for data in mind_update_source:
                doll.doll_mind_update.update_or_create(
                    core=data.get('core'),
                    mind_piece=data.get('mempiece')
                )

            doll.save()
            if doll_create is True:
                print(f'{d_source.get("codename")} 생성 완료')
            else:
                print(f'{d_source.get("codename")} 업데이트 완료')
        self.driver.close()

    def create_equip(self):
        site_source = self.equip_list_add
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/equip.json').json()
        for s_source, d_source in zip(site_source, data_source):
            self.driver.get(self.source_url + s_source)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            if d_source.get('fitGuns'):
                is_private = True
            else:
                is_private = False

            equip_data = {
                'id': d_source.get('id'),
                'codename': d_source.get('codename'),
                'kr_name': soup.select_one('div > div > img + h2').get_text(strip=True),
                'rank': d_source.get('rank'),
                'category': d_source.get('category'),
                'type': d_source.get('type'),
                'company': d_source.get('company'),
                'exclusiveRate': d_source.get('exclusiveRate'),
                'maxLevel': d_source.get('maxLevel'),
                'build_time': d_source.get('buildTime'),
                'is_private': is_private,
            }

            try:
                status_pow = d_source['stats']['pow']['max']
            except KeyError:
                status_pow = 0
            try:
                status_hit = d_source['stats']['hit']['max']
            except KeyError:
                status_hit = 0
            try:
                status_rate = d_source['stats']['rate']['max']
            except KeyError:
                status_rate = 0
            try:
                status_dodge = d_source['stats']['dodge']['max']
            except KeyError:
                status_dodge = 0
            try:
                status_armor = d_source['stats']['armor']['max']
            except KeyError:
                status_armor = 0
            try:
                status_bullet = d_source['stats']['bullet']['max']
            except KeyError:
                status_bullet = 0
            try:
                status_cp = d_source['stats']['criticalPercent']['max']
            except KeyError:
                status_cp = 0
            try:
                status_ch = d_source['stats']['criticalHarmRate']['max']
            except KeyError:
                status_ch = 0
            try:
                status_speed = d_source['stats']['speed']['max']
            except KeyError:
                status_speed = 0
            try:
                status_nv = d_source['stats']['nightview']['max']
            except KeyError:
                status_nv = 0
            try:
                status_ap = d_source['stats']['armorPiercing']['max']
            except KeyError:
                status_ap = 0

            equip_status_data = {
                'pow': status_pow,
                'hit': status_hit,
                'rate': status_rate,
                'dodge': status_dodge,
                'armor': status_armor,
                'bullet': status_bullet,
                'critical_percent': status_cp,
                'critical_harm_rate': status_ch,
                'speed': status_speed,
                'night_view': status_nv,
                'armor_piercing': status_ap,
            }

            equip, equip_create = DollEquip.objects.update_or_create(
                id=d_source.get('id'),
                defaults=equip_data,
            )

            equip.equip_image.save(
                f'{equip_data["codename"]}.png',
                ContentFile(
                    requests.get(f'{self.github_image_base_equip_url}{equip_data["codename"]}.png?raw=true').content)
            )

            equip.doll_equip_status.update_or_create(
                defaults=equip_status_data,
            )

            try:
                fitgun = d_source['fitGuns']
            except KeyError:
                fitgun = []

            for item in fitgun:
                equip.doll_equip_fit.update_or_create(
                    fit_doll_id=item
                )

            equip.save()
            if equip_create is True:
                print(f'{d_source.get("codename")} 생성 완료')
            else:
                print(f'{d_source.get("codename")} 업데이트 완료')
        self.driver.close()

    def create_doll_detail(self):
        context_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-extra-data/master/data/ko/characterScript.json').json()
        for key, c_source in zip(context_source.keys(), context_source.values()):
            doll_context = {
                'drop': None,
                'dialogue1': c_source['default']['DIALOGUE1'],
                'dialogue2': c_source['default']['DIALOGUE2'],
                'dialogue3': c_source['default']['DIALOGUE3'],
                'soul_contract': c_source['default']['SOULCONTRACT'],
                'introduce': c_source['default']['Introduce'],
                'gain': c_source['default'].get('GAIN'),
            }
            c_doll, doll_c_create = DollDetail.objects.update_or_create(
                doll=[item for item in Doll.objects.filter(id=key)][0],
                defaults=doll_context,
            )

            c_doll.save()


if __name__ == '__main__':
    Crawling().create_doll()
    Crawling().create_doll_detail()
    Crawling().create_equip()
