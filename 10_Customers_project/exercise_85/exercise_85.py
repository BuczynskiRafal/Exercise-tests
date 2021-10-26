class CustomersDB:

    def __init__(self, connection):
        self.connection = connection

    def find_customers_by_country(self, country):
        cursor = self.connection.cursor()
        sql = """
            SELECT *
            FROM customers
            WHERE country LIKE :country
            ORDER BY first_name, last_name;"""
        cursor.execute(sql, locals())
        for row in cursor:
            yield row