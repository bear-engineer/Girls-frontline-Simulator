import requests
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('utils/webdriver/chromedriver')


class Crawling:
    def __init__(self, source_url='http://localhost:3000'):
        self.source_url = source_url
        self.doll_id_list = []

    def doll_list_add(self):
        """
        doll id 값 파싱
        :return:
        """
        driver.get(f'{self.source_url}/doll')
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        doll_id = soup.select('div > a')

        for item in doll_id:
            self.doll_id_list.append(item.get('href'))
        return self.doll_id_list

    def create_doll(self):
        site_source = self.doll_list_add()
        data_source = requests.get(
            'https://raw.githubusercontent.com/36base/girlsfrontline-core/master/data/doll.json'
        ).json()

        for s_source, d_source in zip(site_source, data_source):
            driver.get(self.source_url + s_source)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            pass


if __name__ == '__main__':
    Crawling().doll_list_add()
