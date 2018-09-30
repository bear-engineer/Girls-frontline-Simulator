from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos, DollStatus


class Formula:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.center = kwargs.get('center')
        self.effect = [item for item in DollEffect.objects.filter(doll__id=self.id)][0]
        self.effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=self.id)]

    def position(self):
        pass

    def status(self):
        pass

def doll_position(**kwargs):
    """
    전술 인형 중심 위치에따라 자동으로 이펙트 데이터 적용 위치 환산
    들어오는 값
    {'id':id_Number, 'center':center_Number,}
    :param kwargs:
    :return:
    """
    doll_id = kwargs.get('id')
    center = kwargs.get('center')
    doll_effect = [item for item in DollEffect.objects.filter(doll__id=doll_id)][0]
    doll_effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=doll_id)]
    doll_positions = {
    }

    # 포지션 위치값
    pos_list = []
    if center > doll_effect.center:
        values = center - doll_effect.center
        center_position = values + doll_effect.center
        for pos in doll_effect_pos:
            pos_values = pos.pos + values
            if pos.pos + values == 7 or pos.pos + values >= 10 or pos.pos + values == 3:
                pos_values = 0
            doll_positions['center'] = center_position
            pos_list.append(pos_values)
        doll_positions['pos'] = pos_list
    elif center < doll_effect.center:
        values = doll_effect.center - center
        center_position = doll_effect.center - values
        for pos in doll_effect_pos:
            pos_values = pos.pos - values
            if pos_values < 0:
                pos_values = 0
            doll_positions['center'] = center_position
            pos_list.append(pos_values)
        doll_positions['pos'] = pos_list
    else:
        # default center 일 경우
        doll_positions['center'] = center
        doll_positions['pos'] = [item.pos for item in doll_effect_pos]
        doll_positions['type'] = doll_effect.type
    return doll_positions


def doll_status(**kwargs):
    doll_id = kwargs['id']
    status_list = [
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
        for item in DollStatus.objects.filter(doll__id=doll_id)
    ][0]
    return status_list


def formula(data_list):
    """
    전술 인형 위치값을 포함한 계산식
    그리드 이펙트 추가
    들어오는 값
    [
        {
            'id':id_Number,
            'center':center_Number,
        },
        {
            'id':id_Number,
            'center':center_Number,
        },
    ]
    :param data_list:
    :return:
    """

    # 9번까지 그리드 이펙트 저장소 자동 생성
    position_grid_list = [
        {i: {
            'pow': 0,
            'armor': 0,
            'cool_down': 0,
            'critical_percent': 0,
            'dodge': 0,
            'rate': 0,
            'hit': 0,
            'apply_effect_doll_id': [],
        },
        } for i in range(1, 9 + 1)]

    # 해당하는 위치값에 전술인형 넘버를 넣고 이펙트 데이터 합산
    for data in data_list:
        effect_index = 'pow,armor,cool_down,critical_percent,dodge,rate,hit'.split(',')
        effect_grid = [
            {
                'pow': item.pow,
                'armor': item.armor,
                'cool_down': item.cool_down,
                'critical_percent': item.critical_percent,
                'dodge': item.dodge,
                'rate': item.rate,
                'hit': item.hit,
            }
            for item in DollEffectGrid.objects.filter(doll__id=data['id'])
        ][0]

        for position_num in doll_position(**data)['pos']:
            # 값이 0 일경우 무시
            if position_num == 0:
                continue
            position_grid_list[position_num - 1][position_num]['apply_effect_doll_id'].append(data['id'])
            for index in effect_index:
                # 값이 없거나 0 일경우 무시
                if effect_grid[index] is None or 0:
                    continue
                position_grid_list[position_num - 1][position_num][index] += effect_grid[index]

    return position_grid_list
