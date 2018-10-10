from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos, DollStatus, Doll
from tactical_equips.models import DollEquip, DollEquipStatus


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
        self.status_value = 'pow,hit,rate,dodge,armor,bullet,critical_percent,critical_harm_rate,speed,night_view,armor_piercing'.split(
            ',')

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
        # class GetDoll:
        #     """
        #     기초 정보 불러오기
        #     """
        #
        #     def __init__(self, **kwargs):
        #         self.id = kwargs.get('id')
        #         self.center = kwargs.get('center')
        #         self.effect_index = 'pow,armor,cool_down,critical_percent,dodge,rate,hit'.split(',')
        #         self.doll = [item for item in Doll.objects.filter(id=self.id)][0]
        #         self.effect = [item for item in DollEffect.objects.filter(doll__id=self.id)][0]
        #         self.effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=self.id)]
        #         self.doll_status = [item for item in DollStatus.objects.filter(doll__id=self.id)][0]
        #         self.effect_grid = [
        #             {
        #                 'pow': item.pow,
        #                 'armor': item.armor,
        #                 'cool_down': item.cool_down,
        #                 'critical_percent': item.critical_percent,
        #                 'dodge': item.dodge,
        #                 'rate': item.rate,
        #                 'hit': item.hit,
        #             }
        #             for item in DollEffectGrid.objects.filter(doll__id=self.id)
        #         ][0]
        #         self.status_list = [
        #             {
        #                 'kr_name': doll.kr_name,
        #                 'image': doll.image,
        #                 'hp': item.hp,
        #                 'pow': item.pow,
        #                 'hit': item.hit,
        #                 'dodge': item.dodge,
        #                 'speed': item.speed,
        #                 'rate': item.rate,
        #                 'armor_piercing': item.armor_piercing,
        #                 'critical_percent': item.critical_percent,
        #                 'bullet': item.bullet,
        #                 'armor': item.armor,
        #             }
        #             for doll, item in zip(self.doll, self.doll_status)
        #
        #         ][0]
        #
        #     # self.positions = {}
        #
        #     @property
        #     def position(self):
        #         # 포지션 위치값
        #         pos_list = []
        #         if self.center > self.effect.center:
        #             values = self.center - self.effect.center
        #             center_position = values + self.effect.center
        #             for pos in self.effect_pos:
        #                 pos_values = pos.pos + values
        #                 if pos.pos + values == 7 or pos.pos + values >= 10 or pos.pos + values == 3:
        #                     pos_values = 0
        #                 self.positions['center'] = center_position
        #
        #                 # 값이 0 일 경우 추가하지 않는다.
        #                 if pos_values == 0:
        #                     continue
        #                 pos_list.append(pos_values)
        #             self.positions['pos'] = pos_list
        #         elif self.center < self.effect.center:
        #             values = self.effect.center - self.center
        #             center_position = self.effect.center - values
        #             for pos in self.effect_pos:
        #                 pos_values = pos.pos - values
        #                 if pos_values < 0:
        #                     pos_values = 0
        #                 self.positions['center'] = center_position
        #
        #                 # 값이 0 일 경우 추가하지 않는다.
        #                 if pos_values == 0:
        #                     continue
        #                 pos_list.append(pos_values)
        #             self.positions['pos'] = pos_list
        #         else:
        #             # default center 일 경우
        #             self.positions['center'] = self.center
        #             self.positions['pos'] = [item.pos for item in self.effect_pos]
        #         self.positions['type'] = self.effect.type
        #         for grid in self.effect_index:
        #             if self.effect_grid[grid] is None:
        #                 self.effect_grid[grid] = 0
        #         self.positions['effect'] = self.effect_grid
        #         return self.positions
        #
        #
        # class Formula:
        #     def __init__(self, data):
        #         self.data_list = data
        #         self.effect_index = 'pow,armor,cool_down,critical_percent,dodge,rate,hit'.split(',')
        #         self.type_list = 'all,ar,rf,hg,mg,smg,sg'.split(',')
        #         self.position_grid_list = [
        #             {i: {
        #                 'effect': {},
        #                 'apply_effect_doll_id': [],
        #             },
        #             } for i in range(1, 9 + 1)]
        #
        #     def effect_formula(self):
        #         for data in self.data_list:
        #             dept = GetDoll(**data).position
        #             for i in dept.get('pos'):
        #                 self.position_grid_list[i - 1][i]['apply_effect_doll_id'].append(data['id'])
        #                 for index in self.type_list:
        #                     if dept.get('type') == index:
        #                         for grid in self.effect_index:
        #                             try:
        #                                 self.position_grid_list[i - 1][i]['effect'][index][grid] += dept.get('effect')[grid]
        #                             except KeyError:
        #                                 self.position_grid_list[i - 1][i]['effect'][index] = {
        #                                     'pow': dept.get('effect')['pow'],
        #                                     'armor': dept.get('effect')['armor'],
        #                                     'cool_down': dept.get('effect')['cool_down'],
        #                                     'critical_percent': dept.get('effect')['critical_percent'],
        #                                     'dodge': dept.get('effect')['dodge'],
        #                                     'rate': dept.get('effect')['rate'],
        #                                     'hit': dept.get('effect')['hit'],
        #                                 }
        #
        #         return self.position_grid_list
        #
        #     def status_formula(self):
        #         result = []
        #         for data in self.data_list:
        #             status_dict = {}
        #             doll = GetDoll(**data)
        #             try:
        #                 value = self.effect_formula()[doll.position['center'] - 1][doll.position['center']]['effect'][
        #                     doll.position['type']]
        #             except KeyError:
        #                 continue
        #
        #             for index in self.effect_index:
        #                 try:
        #                     status_key = doll.status_list[index]
        #                     if status_key > 0:
        #                         status_dict[index] = 1 + (value[index] * 0.01) * status_key + status_key
        #                 except KeyError:
        #                     status_dict[index] = 0
        #
        #             result.append(status_dict)
        #         return result
        #         # 1 + 15 * 0.01
