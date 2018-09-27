from tactical_dolls.models import DollEffect, DollEffectGrid, DollEffectPos


def doll_effect(**kwargs):
    id = kwargs.get('id')
    center = kwargs.get('center')
    doll_effect = [item for item in DollEffect.objects.filter(doll__id=id)][0]
    doll_effect_pos = [item for item in DollEffectPos.objects.filter(doll__id=id)]
    doll_effect_grid = [item for item in DollEffectGrid.objects.filter(doll__id=id)][0]
    doll_positions = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    doll_postion_grid = {}

    # 포지션 위치값
    if center > doll_effect.center:
        values = center - doll_effect.center
        center_position = values + doll_effect.center
        for pos in doll_effect_pos:
            pos_values = pos.pos + values
            if pos_values < 9:
                pos_values = 0
            doll_positions[center_position].append(pos_values)
    elif center < doll_effect.center:
        values = doll_effect.center - center
        center_position = doll_effect.center - values
        for pos in doll_effect_pos:
            pos_values = pos.pos - values
            if pos_values < 0:
                pos_values = 0
            doll_positions[center_position].append(pos_values)
    else:
        # default center 일 경우
        doll_positions[center] = [item.pos for item in doll_effect_pos]
    return doll_positions


def doll_effect_formula(request):
    id = request.get('id')
    center = request.get('center')
    doll_effect = [item for item in DollEffect.objects.filter(doll__id=id)][0]
    doll_effect_pos = [item.pos for item in DollEffectPos.objects.filter(doll__id=id)][0]
    doll_effect_grid = [item for item in DollEffectGrid.objects.filter(doll__id=id)][0]
    doll_positions = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }
    doll_postion_grid = {}

    # 포지션 위치값
    if center > doll_effect.center:
        values = center - doll_effect.center
        center_position = values + center
        for pos in doll_effect_pos:
            pos_values = pos + values
            if pos_values > 9:
                pos_values = 0
            doll_positions[center_position] += pos_values
    elif center < doll_effect.center:
        values = doll_effect.center - center
        center_position = values - center
        for pos in doll_effect_pos:
            pos_values = pos - values
            if pos_values < 0:
                pos_values = 0
            doll_positions[center_position] += pos_values
    else:
        doll_positions[center] = doll_effect_pos
