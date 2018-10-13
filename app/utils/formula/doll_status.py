from tactical_dolls.models import DollStatus
from tactical_dolls.models import Doll as Doll_query


class Doll:
    def __init__(self, data):
        self.data = data
        self.id = self.data['id']
        self.doll_query = [item for item in Doll_query.objects.filter(id=self.id)]
        self.doll_status_query = [item for item in DollStatus.objects.filter(doll__id=self.id)]
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
        } for item in self.doll_status_query][0]

    @property
    def status_result(self):
        return {
            'id': self.id,
            'codename': [item.codename for item in self.doll_query][0],
            'center': self.data['center'],
            'position': None,
            'status': self.status,
        }
