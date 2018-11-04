class Positions:
    def __init__(self, query):
        self.query_set = query
        self.effect_list = 'pow,hit,rate,dodge,critical_percent,cool_down,armor'.split(',')
        self.relative_position = {
            1: (-1, 1),
            2: (0, 1),
            3: (1, 1),
            4: (-1, 0),
            5: (0, 0),
            6: (1, 0),
            7: (-1, -1),
            8: (0, -1),
            9: (1, -1),
        }
        self.result = []

    def get_position(self):
        for data in self.query_set:
            position_list = data['doll_info']['effect__pos']

            for item in position_list:
                data['position_xy'].append((
                    self.relative_position[data['position']][0] - self.relative_position[item][0],
                    self.relative_position[data['position']][1] - self.relative_position[item][1]
                ))
        return self.query_set

    def position_set_effect(self):
        query = self.get_position()
        result = []
        for data in query:
            doll_position = self.relative_position[data['position']]
            for item in query:
                doll_type = data['doll_info']['type']
                set_effect_type = item['doll_info']['effect__type']

                if doll_type == set_effect_type or item['doll_info']['effect__type'] == 'ALL':
                    if doll_position in item['position_xy']:
                        for effect in self.effect_list:
                            print(effect)
                            effect_set = item['doll_info'][f'effect__effectgrid__{effect}']
                            if effect_set == 0:
                                continue
                            try:
                                data['effect_info'][effect] += item['doll_info'][f'effect__effectgrid__{effect}']
                            except KeyError:
                                data['effect_info'][effect] = item['doll_info'][f'effect__effectgrid__{effect}']

            result.append(data)
        return result
