from utils.formula.effect_position import EffectPos
from .equip import Equip
from .doll_status import Doll


class Formula:
    def __init__(self, data):
        self.data = data
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

        self.effect_status_list = 'pow,' \
                                  'hit,' \
                                  'rate,' \
                                  'dodge,' \
                                  'armor,' \
                                  'bullet,' \
                                  'critical_percent,' \
                                  'critical_harm_rate,' \
                                  'speed,' \
                                  'cool_down'.split(',')
        self.result = []

    @property
    def formula_result(self):
        """
        최종 계산식
        :return:
        """
        for data in self.data:
            status = Doll(data).status_result
            equip_status = Equip(data).equip_result

            # doll status + doll equip status formula
            for item in self.status_list:
                status['status'][item] += equip_status[item]

            # effect pos add
            status['effect_position'] = EffectPos(data).effect_position_result

            # return list add
            self.result.append(status)
        return self.result
