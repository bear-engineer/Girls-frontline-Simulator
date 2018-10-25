from tactical_dolls.models import DollStatus


class Doll:
    """
    doll info & status data export
    """

    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        self.doll_query = DollStatus.objects.select_related('doll').filter(doll__id=self.id)
        self.status = [{
            'hp': item.hp,
            'pow': item.pow,
            'hit': item.hit,
            'dodge': item.dodge,
            'rate': item.rate,
            'speed': item.speed,
            'armor_piercing': item.armor_piercing,
            'critical_harm_rate': item.critical_harm_rate,
            'critical_percent': item.critical_percent,
            'bullet': item.bullet,
            'night_vision': item.night_view,
            'armor': item.armor,
        } for item in self.doll_query][0]

    @property
    def status_result(self):
        return {
            'id': self.id,
            'codename': [item.doll.codename for item in self.doll_query][0],
            'image': [item.doll.image.url for item in self.doll_query][0],
            'type': [item.doll.type for item in self.doll_query][0],
            'center': self.data['center'],
            'effect_position': None,
            'effect_status': None,
            'status': self.status,
        }
