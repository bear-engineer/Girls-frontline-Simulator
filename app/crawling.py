import os

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import django

# 장고 모듈 import
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

            # 개조된 인형을 구
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
                'hp': d_source['stats'].get('hp'),
                'pow': d_source['stats'].get('pow'),
                'hit': d_source['stats'].get('hit'),
                'dodge': d_source['stats'].get('dodge'),
                'speed': d_source['stats'].get('speed'),
                'rate': d_source['stats'].get('rate'),
                'armor_piercing': d_source['stats'].get('armorPiercing'),
                'critical_percent': d_source['stats'].get('criticalPercent'),
                'bullet': doll_status_bullet,
                'armor': doll_status_armor,
            }
            pass


if __name__ == '__main__':
    Crawling().create_doll()
