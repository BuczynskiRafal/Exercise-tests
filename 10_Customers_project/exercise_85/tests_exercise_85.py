import unittest
from sqlite3 import connect
from exercise_85 import CustomersDB


class TestCustomersDB(unittest.TestCase):

    def setUp(self):
        connection = connect(':memory:')
        cursor = connection.cursor()

        create_table_sql = """
            CREATE TABLE customers 
            ( 
                first_name TEXT, 
                last_name  TEXT, 
                email      TEXT, 
                phone      TEXT, 
                country    TEXT 
            );"""
        cursor.execute(create_table_sql)

        customers_data = [
            ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
            ('John', 'Doe', 'john.doe@mail.com', '333', 'Canada'),
            ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        ]

        insert_sql = """
            INSERT INTO customers
            VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(insert_sql, customers_data)

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_customer_by_country(self):
        db = CustomersDB(self.connection)
        actual = tuple(db.find_customers_by_country('USA'))
        expected = (
         ('John', 'Smith', 'john.smith@mail.com', '111', 'USA'),
         ('Mike', 'Doe', 'mike.doe@mail.com', '222', 'USA')
        )
        self.assertEqual(actual, expected)