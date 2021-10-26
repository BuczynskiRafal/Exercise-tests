class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def find_customers_by_first_name(self, first_name):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE first_name LIKE :first_name
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row