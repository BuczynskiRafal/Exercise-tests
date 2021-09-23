import unittest

class TestSplitMethod(unittest.TestCase):
    
    
    def test_split_by_default(self):
        self.assertEqual('Python Testing'.split(), ['Python', 'testing'])
    
    def test_split_by_comma(self):
        self.assertEqual('open,high,low,close'.split(','), ['open','high','low','close'])
    
    def test_split_by_hash(self):
        self.assertEqual('summer#time#vibes'.split('#'), ['summer', 'time', 'vibes'])
        
# %%

import unittest

class TestJoinMethod(unittest.TestCase):
    
    
    def test_join_with_space(self):
        var1 = ' '.join(['Python', '3.8'])
        var2 = 'Python 3.8'
        self.assertEqual(var1, var2)
        
    def test_join_with_comma(self):
        var1 = ','.join(['open','high','low','close'])
        var2 = 'open,high,low,close'
        self.assertEqual(var1, var2)
        
    def test_join_with_new_line_char(self):
        var1 = '\n'.join(['open','high','low','close'])
        var2 = 'open\high\low\close'
        self.assertEqual(var1, var2)
        
#%%
import unittest


class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python3.8')

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)

        
        
TestJoinMethod.test_join_with_space()     
        
#%%
import unittest
from collections import Counter


class TestIsInstance(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance((), tuple))

    def test_case_2(self):
        self.assertTrue(isinstance([], list))

    def test_case_3(self):
        self.assertTrue(isinstance({}, dict))

    def test_case_4(self):
        cnt = Counter()
        self.assertTrue(isinstance(cnt, Counter))

    def test_case_5(self):
        var1 = 4
        self.assertTrue(isinstance(var1, int))

    def test_case_6(self):
        var2 = 4,
        self.assertTrue(isinstance(var2, tuple))

#%%
import unittest


class TestUpper(unittest.TestCase):
    
    
    def test_upper(self):
        self().assertEqual('summer'.upper(), 'SUMMER')
        
    def test_is_upper(self):
        self.assertEqual('SUMMER'.isupper(), True)
        self.assertEqual('summer'.isupper(), False)

# %%

import unittest



class TestLower(unittest.TestCase):
    

    def test_lower(self):
        self.assertEqual('Joe.Smith@mail.com'.lower(), 'joe.smith@mail.com')
        
    def test_is_lower(self):
        self.assertTrue('joe.smith@mail.com'.islower())
        self.assertFalse('Joe.Smith@mail.com'.islower())


# %%
import unittest



class TestStartswithMethod(unittest.TestCase):
    
    
    def test_startswith_one_letter(self):
        self.assertTrue('unittest'.startswith('u'))
        self.assertFalse('unittest'.startswith('U'))
        
    def test_startswith_four_letters(self):
        self.assertTrue('https://e-smartdata.org/'.startswith('http')) 
        self.assertTrue('www.e-smartdata.org/'.startswith('http')) 
    
    
    
    
class TestEndswithMethod(unittest.TestCase):
    
    
    def test_endswith_three_letter(self):
        self.assertTrue('e-smartdata.org/'.endswith('org'))
        self.assertFalse('e-smartdata.org/'.endswith('com'))

# %%
import unittest
class TertLstripMethod(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(' str'.lstrip())
        self.assertFalse('str'.lstrip())
    
class TertStripMethod(unittest.TestCase):
    def test_case_2(self):
        self.assertTrue(' str '.strip())
        self.assertFalse('str'.strip())

class TertRstripMethod(unittest.TestCase):
    def test_case_3(self):
        self.assertTrue('str_'.rstrip())
        self.assertFalse('str'.rstrip())

# %%
import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, )


class TestCalculateDailyReturn(unittest.TestCase):
    
    
    def test_positive_return(self):
        self.assertEqual(calculate_daily_return(349, 360), 3.15)
        
    def test_negative_return(self):    
        self.assertEqual(calculate_daily_return(349, 340), -2.58)
        
    def test_zero_return(self):
        self.assertEqual(calculate_daily_return(349, 349), 0.0)

# %%
import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, )


class TestCalculateDailyReturn(unittest.TestCase):
    
    
    def test_positive_return(self):
        self.assertAlmostEqual(calculate_daily_return(349, 360), 3.15)
        
    def test_negative_return(self):    
        self.assertAlmostEqual(calculate_daily_return(349, 340), -2.58)
        
    def test_zero_return(self):
        self.assertAlmostEqual(calculate_daily_return(349, 349), 0.0)

#%%
import unittest


class Doc:

    def __init__(self, string):
        self.string = string
        
    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __lt__(self, other):
        return len(self.string) < len(other.string)



class TestDoc(unittest.TestCase):
    def test_less_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertLess(doc2, doc1)
        self.assertLess(doc3, doc1)
    
    def test_greater_than(self):
        doc1 = Doc('Technology')
        doc2 = Doc('Online')
        doc3 = Doc('Nature')
        self.assertGreater(doc1, doc2)
        self.assertGreater(doc2, doc2)

#%%
import unittest


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __eq__(self, other):
        return len(self.string) == len(other.string)

class TestDoc(unittest.TestCase):
    def test_equal(self):
        doc3 = Doc('Technology')
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertEqual(doc1, doc2)

    def test_not_equal(self):
        doc3 = Doc('Technology')
        doc1 = Doc('Online')
        doc2 = Doc('Nature')
        self.assertNotEqual(doc3, doc1)
        self.assertNotEqual(doc3, doc2)

#%%
import unittest


class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))

class TestEmployee(unittest.TestCase):
    def test_has_email_attr(self):
        msg = 'The Employee class does not have an email attribute.'
        self.assertTrue(Employee.hasattr(), 'email', msg)
    
    def test_has_tax_attr(self):
        msg = 'The Employee class does not have a tax attribute.'
        self.assertTrue(Employee.hasattr(), 'tax', msg)

    def test_has_apply_bonus(self):
        msg = 'The Employee class does not have an apply_bonus attribute.'
        self.assertTrue(Employee.hasattr(), 'apply_bonus', msg)

#%% 
import unittest


class Employee:
    """A simple class that describes an employee of the company."""

    tax_rate = 0.17
    bonus_rate = 0.10

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@mail.com'

    @property
    def tax(self):
        return round(self.salary * self.tax_rate, 2)

    def apply_bonus(self):
        self.salary = int(self.salary * (1 + self.bonus_rate))

class TestEmploye(unittest.TestCase):
    def test_has_email_attr(self):
        msg = 'The Employee class does not have an email attribute.'
        self.assertTrue(hasattr(Employee, 'email'), msg)
    def test_has_email_property(self):
        self.assertIsInstance(Employee.email, property)

#%%
import unittest


class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only object of type str can be added to the list.')
        super().append(string)


class TestStringListOnly(unittest.TestCase):
    def test_append_string(self):
        slo = StringListOnly()
        string = 'big_data'
        slo.append(string)
        self.assertIn(string, slo)

    def test_append_not_string_should_raise_error(self):
        slo = StringListOnly()
        var1 = ['list']
        var2 = [None]
        self.assertRaises(TypeError, slo.append, var1)
        self.assertRaises(TypeError, slo.append, var2)






















        