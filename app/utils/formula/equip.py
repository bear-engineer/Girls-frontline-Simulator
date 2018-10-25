from rest_framework import status

from tactical_dolls.models import Doll
from tactical_equips.models import DollEquipStatus, DollEquipFit, DollEquip
from utils.custom_exception import CustomException

__all__ = (
    'Equip',
)


class Equip:
    """
    유효한 equip 인지 확인 및 validate 통과시 모듈 status 합산, 반환
    """

    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        self.slot_id_list = []
        self.status_list = 'pow,' \
                           'hit,' \
                           'rate,' \
                           'dodge,' \
                           'armor,' \
                           'bullet,' \
                           'critical_percent,' \
                           'critical_harm_rate,' \
                           'speed,' \
                           'night_vision,' \
                           'armor_piercing'.split(',')

    def slot_id(self):
        """
        equip id value 순회 가능한 객체 만들어주기
        :return:
        """
        for num in range(1, 3 + 1):
            if not self.data[f'slot_0{num}']:
                continue
            else:
                self.slot_id_list.append(self.data[f'slot_0{num}'])
        return self.slot_id_list

    def doll_equip_query(self, data):
        return DollEquipStatus.objects.select_related('equip').filter(equip__id=data)

    def validate(self):
        """
        유효한 모듈인지 검사
        :return:
        """

        # 해당 전술 인형이 장착 할 수 있는 모듈인지 확인
        equip_slot = [
            {
                'slot_01': item.equip_slot_01,
                'slot_02': item.equip_slot_02,
                'slot_03': item.equip_slot_03,
            } for item in Doll.objects.filter(id=self.id)
        ][0]
        for num in range(1, 3 + 1):
            # 해당 필드가 None 일 경우 실행하지 않고 넘어감
            if not self.data[f'slot_0{num}']:
                continue

            # Doll Equip type, string 값 비교
            # DollEquip.objects.filter(id=self.data[f'slot_0{num}'])
            equip_type = [value.equip.type for value in self.doll_equip_query(self.data[f'slot_0{num}'])][0]
            if str(equip_type) in equip_slot[f'slot_0{num}']:
                pass
            else:
                raise CustomException(detail='해당하는 전술인형에 유효한 모듈이 아닙니다.', status_code=status.HTTP_400_BAD_REQUEST)

        fit_gun_result = False
        for item in self.slot_id():
            # DollEquip.objects.filter(id=item)
            equip_objects = [value.equip for value in self.doll_equip_query(item)][0]

            # 전용장비 검사
            private = equip_objects.is_private
            if private is True:
                fit_gun = [value.fit_doll_id for value in DollEquipFit.objects.filter(equip__id=item)]
                for fit_gun_id in fit_gun:
                    if self.id != fit_gun_id:
                        continue
                    else:
                        fit_gun_result = True
                if fit_gun_result is False:
                    raise CustomException(detail='해당 모듈은 전용장비입니다. 알맞은 전술 인형에 장착하세요',
                                          status_code=status.HTTP_400_BAD_REQUEST)
                else:
                    pass
        return self.slot_id()

    @property
    def equip_result(self):
        """
        all equip 합산
        :return:
        """
        # result dict 초기화
        result = {}
        for item in self.status_list:
            result[item] = 0

        # result dict 에 합산
        for item in self.validate():
            slot_status = [{
                'pow': value.pow,
                'hit': value.hit,
                'rate': value.rate,
                'dodge': value.dodge,
                'armor': value.armor,
                'bullet': value.bullet,
                'critical_percent': value.critical_percent,
                'critical_harm_rate': value.critical_harm_rate,
                'speed': value.speed,
                'night_vision': value.night_view,
                'armor_piercing': value.armor_piercing,
                # DollEquipStatus.objects.filter(equip__id=item)
            } for value in self.doll_equip_query(item)][0]
            for status_value in self.status_list:
                result[status_value] += slot_status[status_value]
        return result
