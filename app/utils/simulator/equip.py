from utils.custom_exception import CustomException


class EquipCalculation:
    def __init__(self, query, data):
        self.query = query
        self.data = data
        self.slot_list = 'slot_01,slot_02,slot_03'.split(',')
        self.status_list = 'pow,hit,dodge,rate,armor,critical_harm_rate,critical_percent,bullet,speed,night_view'.split(
            ',')

    def equip_calculation(self):
        for data in self.query:
            for item in self.slot_list:
                equip_info = self.data[data['id']][item]
                if not equip_info:
                    continue
                if equip_info['type'] in data[item]:
                    for status_name in self.status_list:
                        try:
                            data[f'status__{status_name}'] += equip_info[status_name]
                        except KeyError:
                            continue
                else:
                    raise CustomException(
                        detail=f'모듈 {equip_info["code_name"]} 은/는{data["code_name"]} 전술인형에 유효한 모듈이 아닙니다.',
                    )
        return self.query
