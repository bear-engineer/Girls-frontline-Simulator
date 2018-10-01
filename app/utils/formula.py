from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos, DollStatus


class GetDoll:
    """
    기초 정보 불러오기
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.center = kwargs.get('center')
        self.effect_index = 'pow,armor,cool_down,critical_percent,dodge,rate,hit'.split(',')
        self.effect = [item for item in DollEffect.objects.filter(doll__id=self.id)][0]
        self.effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=self.id)]
        self.effect_grid = [
            {
                'pow': item.pow,
                'armor': item.armor,
                'cool_down': item.cool_down,
                'critical_percent': item.critical_percent,
                'dodge': item.dodge,
                'rate': item.rate,
                'hit': item.hit,
            }
            for item in DollEffectGrid.objects.filter(doll__id=self.id)
        ][0]
        self.status_list = [
            {
                'hp': item.hp,
                'pow': item.pow,
                'hit': item.hit,
                'dodge': item.dodge,
                'speed': item.speed,
                'rate': item.rate,
                'armor_piercing': item.armor_piercing,
                'critical_percent': item.critical_percent,
                'bullet': item.bullet,
                'armor': item.armor,
            }
            for item in DollStatus.objects.filter(doll__id=self.id)
        ][0]
        self.positions = {}

    @property
    def position(self):
        # 포지션 위치값
        pos_list = []
        if self.center > self.effect.center:
            values = self.center - self.effect.center
            center_position = values + self.effect.center
            for pos in self.effect_pos:
                pos_values = pos.pos + values
                if pos.pos + values == 7 or pos.pos + values >= 10 or pos.pos + values == 3:
                    pos_values = 0
                self.positions['center'] = center_position

                # 값이 0 일 경우 추가하지 않는다.
                if pos_values == 0:
                    continue
                pos_list.append(pos_values)
            self.positions['pos'] = pos_list
        elif self.center < self.effect.center:
            values = self.effect.center - self.center
            center_position = self.effect.center - values
            for pos in self.effect_pos:
                pos_values = pos.pos - values
                if pos_values < 0:
                    pos_values = 0
                self.positions['center'] = center_position

                # 값이 0 일 경우 추가하지 않는다.
                if pos_values == 0:
                    continue
                pos_list.append(pos_values)
            self.positions['pos'] = pos_list
        else:
            # default center 일 경우
            self.positions['center'] = self.center
            self.positions['pos'] = [item.pos for item in self.effect_pos]
        self.positions['type'] = self.effect.type
        for grid in self.effect_index:
            if self.effect_grid[grid] is None:
                self.effect_grid[grid] = 0
        self.positions['effect'] = self.effect_grid
        return self.positions


class Formula:
    def __init__(self, data):
        self.data_list = data
        self.effect_index = 'pow,armor,cool_down,critical_percent,dodge,rate,hit'.split(',')

        self.position_grid_list = [
            {i: {
                'effect': {
                    'all': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'ar': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'rf': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'hg': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'mg': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'smg': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                    'sg': {
                        'pow': 0,
                        'armor': 0,
                        'cool_down': 0,
                        'critical_percent': 0,
                        'dodge': 0,
                        'rate': 0,
                        'hit': 0,
                    },
                },
                'apply_effect_doll_id': [],
            },
            } for i in range(1, 9 + 1)]

    def effect_formula(self):
        type_list = 'all,ar,rf,hg,mg,smg,sg'.split(',')
        for data in self.data_list:
            dept = GetDoll(**data).position
            for i in dept.get('pos'):
                self.position_grid_list[i - 1][i]['apply_effect_doll_id'].append(data['id'])
                for index in type_list:
                    if dept.get('type') == index:
                        for grid in self.effect_index:
                            self.position_grid_list[i - 1][i]['effect'][index][grid] += dept.get('effect')[grid]
        return self.position_grid_list
