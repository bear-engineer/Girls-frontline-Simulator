import math

from .effect_position import *
from .equip import *
from .doll_status import *
from .effect_grid import *


class Formula:
    """
    계산식 모듈 종합
    """

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

            # effect grid add
            status['effect_status'] = EffectGrid(data).effect_grid_result
            # return list add
            self.result.append(status)

            # effect formula
            for pos in self.result:
                for center in self.result:
                    if center['center'] in pos['effect_position']['position'] and center['type'] == \
                            pos['effect_position']['type'] or pos['effect_position']['type'] == 'ALL':
                        for item in self.effect_status_list:

                            # exception effect formula
                            try:
                                value = center['status'][item] * (1 + (pos['effect_status'][item] * 0.01))
                                center['status'][item] += value

                                # formula transfer
                                if item == 'pow':
                                    center['status'][item] = math.ceil(center['status'][item])
                                elif item == 'armor' or 'rate' or 'dodge' or 'hit':
                                    center['status'][item] = math.floor(center['status'][item])

                            except KeyError:
                                center['status'][item] = pos['effect_status'][item]
                    else:
                        continue
        return self.result
