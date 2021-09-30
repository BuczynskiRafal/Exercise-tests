import random
from unittest.mock import patch


class Programmer:

    def __init__(self):
        self.tech_names = []

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if not name in self.tech_names:
            self.tech_names.append(name)
            return self
        return self

    def get_random_tech(self):
        return random.choice(self.tech_names)


programmer = Programmer()
programmer.add_tech('python') \
    .add_tech('sql') \
    .add_tech('java') \
    .add_tech('c++') \
    .add_tech('aws')

with patch('random.choice') as mock_random:
    mock_random.return_value = 'sql'
    print(programmer.get_random_tech())