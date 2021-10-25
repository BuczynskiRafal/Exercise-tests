import random
from unittest.mock import Mock


techs = ['python', 'sql', 'java', 'aws', 'c++']

random.choice = Mock(return_value='aws')
print(random.choice())