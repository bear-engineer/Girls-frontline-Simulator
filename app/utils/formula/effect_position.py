from tactical_dolls.models import DollEffect, DollEffectPos


class EffectPos:
    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        self.center = self.data['center']
        self.doll_effect_query = [item for item in DollEffect.objects.filter(doll__id=self.id)][0]
        self.doll_effect_pos_query = [item.pos for item in DollEffectPos.objects.filter(doll__id=self.id)]

    @property
    def effect_position_result(self):
        pos_result = []
        top_position = [3, 6, 9]
        bottom_position = [1, 4, 7]
        default_pos_list = self.doll_effect_pos_query
        if self.center == 1 or self.center == 4 or self.center == 7:
            for rm in bottom_position:
                if rm in default_pos_list:
                    default_pos_list.remove(rm)
        elif self.center == 3 or self.center == 6 or self.center == 9:
            for rm in top_position:
                if rm in default_pos_list:
                    default_pos_list.remove(rm)

        if self.center > self.doll_effect_query.center:
            value = self.center - self.doll_effect_query.center
            for pos in default_pos_list:
                pos_value = pos + value
                if pos_value != 0:
                    pos_result.append(pos_value)
        elif self.center < self.doll_effect_query.center:
            value = self.doll_effect_query.center - self.center
            for pos in default_pos_list:
                pos_value = pos - value
                if pos_value > 0:
                    pos_result.append(pos_value)
        else:
            for pos in default_pos_list:
                pos_result.append(pos)
        return {
            'type': self.doll_effect_query.type,
            'position': pos_result
        }
