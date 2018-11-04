import math

from django.utils.functional import cached_property


class Status:
    def __init__(self, query):
        self.query = query
        self.grow_data = {
            "after100": {
                "basic": {
                    "armor": [13.979, 0.04],
                    "hp": [96.283, 0.138]
                },
                "grow": {
                    "dodge": [0.075, 22.572],
                    "hit": [0.075, 22.572],
                    "pow": [0.06, 18.018],
                    "rate": [0.022, 15.741]
                }
            },
            "normal": {
                "basic": {
                    "armor": [2, 0.161],
                    "dodge": [5],
                    "hit": [5],
                    "hp": [55, 0.555],
                    "pow": [16],
                    "rate": [45],
                    "speed": [10]
                },
                "grow": {
                    "dodge": [0.303, 0],
                    "hit": [0.303, 0],
                    "pow": [0.242, 0],
                    "rate": [0.181, 0]
                }
            }
        }
        self.attr_data = {
            "hg": {
                "hp": 0.6,
                "pow": 0.6,
                "rate": 0.8,
                "speed": 1.5,
                "hit": 1.2,
                "dodge": 1.8
            },
            "smg": {
                "hp": 1.6,
                "pow": 0.6,
                "rate": 1.2,
                "speed": 1.2,
                "hit": 0.3,
                "dodge": 1.6
            },
            "rf": {
                "hp": 0.8,
                "pow": 2.4,
                "rate": 0.5,
                "speed": 0.7,
                "hit": 1.6,
                "dodge": 0.8
            },
            "ar": {
                "hp": 1,
                "pow": 1,
                "rate": 1,
                "speed": 1,
                "hit": 1,
                "dodge": 1
            },
            "mg": {
                "hp": 1.5,
                "pow": 1.8,
                "rate": 1.6,
                "speed": 0.4,
                "hit": 0.6,
                "dodge": 0.6
            },
            "sg": {
                "hp": 2.0,
                "pow": 0.7,
                "rate": 0.4,
                "speed": 0.6,
                "hit": 0.3,
                "dodge": 0.3,
                "armor": 1
            }
        }

    @cached_property
    def formula(self):
        level = 100
        # favor = 100
        dummy = 5

        for item in self.query:

            status_list = 'hp,armor,hit,pow,dodge,rate'.split(',')
            doll_type = item['type'].lower()
            grow = item['grow']
            for stats in status_list:
                doll_status = float(item[f'status__{stats}'])
                if stats == 'hp' or stats == 'armor':
                    try:
                        attr_data = float(self.attr_data[doll_type][stats])
                    except KeyError:
                        continue
                    if level <= 100:
                        basic_data0 = float(self.grow_data['normal']['basic'][stats][0])
                        basic_data1 = float(self.grow_data['normal']['basic'][stats][1])
                        basic_formula = math.ceil(
                            (basic_data0 + ((level - 1) * basic_data1)) * attr_data * doll_status / 100
                        )
                        item[f'status__{stats}'] = basic_formula * dummy
                    else:
                        basic_data0 = float(self.grow_data['after100']['basic'][stats][0])
                        basic_data1 = float(self.grow_data['after100']['basic'][stats][1])
                        basic_formula = math.ceil(
                            (basic_data0 + ((level - 1) * basic_data1)) * attr_data * doll_status / 100
                        )
                        item[f'status__{stats}'] = basic_formula * dummy
                else:
                    attr_data = float(self.attr_data[doll_type][stats])

                    grow_data0 = float(self.grow_data['after100']['grow'][stats][0])
                    grow_data1 = float(self.grow_data['after100']['grow'][stats][1])

                    normal_basic = self.grow_data['normal']['basic'][stats]

                    normal_basic_formula = math.ceil(
                        normal_basic[0] * attr_data * doll_status / 100
                    )
                    normal_grow_formula = math.ceil(
                        (grow_data1 + ((level - 1) * grow_data0)) * attr_data * doll_status * grow / 100 / 100
                    )

                    item[f'status__{stats}'] = normal_basic_formula + normal_grow_formula

        return self.query
