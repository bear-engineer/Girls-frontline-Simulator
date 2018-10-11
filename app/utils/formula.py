from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos, DollStatus, Doll
from tactical_equips.models import DollEquip, DollEquipStatus
import math


class EffectFormula:
    """
    들어오는 값:
        [
            {
                'id':1,
                'center:5,
                'equip_slot_01':5,
                'equip_slot_02':5,
                'equip_slot_03':None,
                },
            {
                'id':2,
                'center:6,
                'equip_slot_01':5,
                'equip_slot_02':1,
                'equip_slot_03':None,
                },
        ]
    limit dict len: 5, 초과시에 에러
    """

    def __init__(self, data):
        self.data = data
        self.status_value = 'pow,' \
                            'hit,' \
                            'rate,' \
                            'dodge,' \
                            'armor,' \
                            'bullet,' \
                            'critical_percent,' \
                            'critical_harm_rate,' \
                            'speed,night_view,' \
                            'armor_piercing'.split(',')
        self.grid_effect_value = 'pow,hit,rate,dodge,critical_percent,cool_down,armor'.split(',')
        self.type = 'all,ar,rf,sg,smg,mg,hg'.split(',')

    def equip_validate(self):
        """
        해당하는 인형의 장비 유효성 검사
        :return:
        """

        # 제대인원 5명 초과시 에러
        if len(self.data) > 5:
            raise ValueError('제대 인원의 한계 인원을 초과하였습니다.')

        for equip in self.data:
            equip_slot = [
                {
                    'equip_slot_01': item.equip_slot_01,
                    'equip_slot_02': item.equip_slot_02,
                    'equip_slot_03': item.equip_slot_03,
                } for item in Doll.objects.filter(id=equip['id'])
            ][0]
            for num in range(1, 3 + 1):
                if equip[f'equip_slot_0{num}'] is None:
                    equip_data = None
                else:
                    equip_data = [item.type for item in DollEquip.objects.filter(id=equip[f'equip_slot_0{num}'])][0]
                if str(equip_data) in equip_slot[f'equip_slot_0{num}'] or equip_data is None:
                    pass
                else:
                    raise ValueError('해당하는 전술인형에 유효한 모듈이 아닙니다.')
        return self.data

    def status_equip_formula(self):
        """
        equip status + doll status

        :return:
        """
        equip_result = []
        status_result = []

        # 전술인형 장비 유효성 검사 사전 실행
        for data in self.equip_validate():
            equip_status = {}
            for num in range(1, 3 + 1):
                if data[f'equip_slot_0{num}'] is not None:
                    equip_status_value = [
                        {
                            'pow': item.pow,
                            'hit': item.hit,
                            'rate': item.rate,
                            'dodge': item.dodge,
                            'armor': item.armor,
                            'bullet': item.bullet,
                            'critical_percent': item.critical_percent,
                            'critical_harm_rate': item.critical_harm_rate,
                            'speed': item.speed,
                            'night_view': item.night_view,
                            'armor_piercing': item.armor_piercing,
                        }
                        for item in DollEquipStatus.objects.filter(equip__id=data[f'equip_slot_0{num}'])][0]

                    for item in self.status_value:
                        try:
                            equip_status[item] += equip_status_value[item]
                        except KeyError:
                            equip_status[item] = equip_status_value[item]
                else:
                    for item in self.status_value:
                        equip_status[item] = 0
            equip_status['id'] = data['id']
            equip_status['center'] = data['center']
            equip_result.append(equip_status)

        for data in equip_result:

            doll_status_value = [
                {
                    'pow': item.pow,
                    'hit': item.hit,
                    'rate': item.rate,
                    'dodge': item.dodge,
                    'armor': item.armor,
                    'bullet': item.bullet,
                    'critical_percent': item.critical_percent,
                    'critical_harm_rate': 0,
                    'speed': item.speed,
                    'night_view': 0,
                    'armor_piercing': item.armor_piercing,
                }
                for item in DollStatus.objects.filter(doll__id=data['id'])][0]
            for item in self.status_value:
                doll_status_value[item] += data[item]

            doll_status_value['id'] = data['id']
            doll_status_value['type'] = [item.type for item in DollEffect.objects.filter(doll__id=data['id'])][0]
            doll_status_value['center'] = data['center']
            # doll_status_value['center'] = data['center']
            status_result.append(doll_status_value)
        return status_result

    def position_formula(self):
        position_result = []
        for data in self.equip_validate():
            doll_position_value = {}
            doll_effect = [{'center': item.center, 'type': item.type} for item in
                           DollEffect.objects.filter(doll__id=data['id'])][0]
            doll_effect_pos = [item.pos for item in DollEffectPos.objects.filter(doll__id=data['id'])]
            pos_result = []

            def validate_list():
                """
                들어오는 center 위치에 따른 position 변화
                :return:
                """

                if doll_effect['center'] == 2 or doll_effect['center'] == 5 or doll_effect['center'] == 8:
                    validate_list_minus = [7, 4, 1]
                    validate_list_plus = [9, 6, 3]
                    if data['center'] == 1 or data['center'] == 4 or data['center'] == 7:
                        for rm_list in validate_list_minus:
                            if rm_list in doll_effect_pos:
                                doll_effect_pos.remove(rm_list)
                    elif data['center'] == 3 or data['center'] == 6 or data['center'] == 9:
                        for rm_list in validate_list_plus:
                            if rm_list in doll_effect_pos:
                                doll_effect_pos.remove(rm_list)
                elif doll_effect['center'] == 3 or doll_effect['center'] == 6 or doll_effect['center'] == 9:
                    validate_list_minus = [1, 4, 7]
                    if data['center'] == 1 or data['center'] == 4 or data['center'] == 7:
                        for rm_list in validate_list_minus:
                            if rm_list in doll_effect_pos:
                                doll_effect_pos.remove(rm_list)
                    if data['center'] == 2 or data['center'] == 5 or data['center'] == 8:
                        for rm_list in validate_list_minus:
                            if rm_list in doll_effect_pos:
                                doll_effect_pos.remove(rm_list)

            if data['center'] > doll_effect['center']:
                validate_list()
                values = data['center'] - doll_effect['center']
                for pos in doll_effect_pos:
                    pos_value_result = pos + values
                    if pos_value_result != 0:
                        pos_result.append(pos_value_result)

            elif data['center'] < doll_effect['center']:
                validate_list()
                values = doll_effect['center'] - data['center']
                for pos in doll_effect_pos:
                    pos_value_result = pos - values
                    if pos_value_result > 0:
                        pos_result.append(pos_value_result)
            else:
                for pos in doll_effect_pos:
                    pos_result.append(pos)
            doll_position_value['id'] = data['id']
            doll_position_value['center'] = data['center']
            doll_position_value['type'] = doll_effect['type']
            doll_position_value['position'] = pos_result
            position_result.append(doll_position_value)

        return position_result

    def grid_formula(self):
        grid_result = [{item: [{types: {} for types in self.type}][0] for item in range(1, 9 + 1)}][0]
        for data in self.position_formula():
            grid_effect = [{
                'pow': item.pow,
                'hit': item.hit,
                'rate': item.rate,
                'dodge': item.dodge,
                'critical_percent': item.critical_percent,
                'cool_down': item.cool_down,
                'armor': item.armor
            } for item in DollEffectGrid.objects.filter(doll__id=data['id'])][0]
            for in_position in data['position']:
                for item in self.grid_effect_value:
                    if grid_effect[item] is None:
                        continue
                    try:
                        grid_result[in_position][data['type']][item] += grid_effect[item]
                    except KeyError:
                        grid_result[in_position][data['type']][item] = grid_effect[item]
        return grid_result

    def status_equip_effect_formula(self):
        result = []
        for data in self.status_equip_formula():
            value = {
                'id': data['id'],
                'type': data['type'],
                'center': data['center'],
                'armor_piercing': data['armor_piercing'],
            }

            for item in self.grid_effect_value:
                try:
                    value[item] = data[item] * (1 + (self.grid_formula()[data['center']][data['type']][item] * 0.01))
                    if item == 'pow':
                        value[item] = math.ceil(value[item])
                    elif item == 'armor' or 'rate' or 'dodge' or 'hit':
                        value[item] = math.floor(value[item])
                except KeyError:
                    try:
                        value[item] = data[item]
                    except KeyError:
                        continue
                    continue
            result.append(value)
        return result

        #         # 1 + 15 * 0.01
