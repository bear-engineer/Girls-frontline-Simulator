from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos


def doll_position(**kwargs):
    """
    re position
    :param kwargs:
    :return:
    """
    id = kwargs.get('id')
    center = kwargs.get('center')
    doll_effect = [item for item in DollEffect.objects.filter(doll__id=id)][0]
    doll_effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=id)]
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
    return doll_positions


def formula(data_list):
    doll_data = []
    for data in data_list:
        dolls = {}
        dolls['id'] = data['id']
        dolls['position'] = doll_position(**data)
        dolls['status'] = [{'pow': item.pow, 'armor': item.armor, 'cool_down': item.cool_down,
                            'critical_percent': item.critical_percent, 'dodge': item.dodge, 'rate': item.rate,
                            'hit': item.hit}
                           for item in DollEffectGrid.objects.filter(doll__id=data['id'])]

        doll_data.append(dolls)
    return doll_data
