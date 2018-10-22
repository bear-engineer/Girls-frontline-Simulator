from tactical_dolls.models import DollEffectGrid


class EffectGrid:
    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        self.center = self.data['center']

    def effect_grid_result(self):
        result = [{
            'pow': item.pow,
            'hit': item.hit,
            'rate': item.rate,
            'dodge': item.dodge,
            'armor': item.armor,
            'bullet': 0,
            'critical_percent': item.critical_percent,
            'critical_harm_rate': 0,
            'speed': 0,
            'cool_down': item.cool_down,
        } for item in DollEffectGrid.objects.filter(doll__id=self.id)][0]

        # 값이 None 일 경우 0으로 치환
        for item in result:
            if not result[item]:
                result[item] = 0
        return result
