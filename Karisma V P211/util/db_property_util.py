# db_property_util.py
class DBPropertyUtil:
    @staticmethod
    def get_property_string():
        host = "LAPTOP-GTBRN9BR\\SQLEXPRESS"
        dbname = "hospitalmanagementdb"

        connection_string = (f'DRIVER={{SQL Server}};'
                             f'SERVER={host};'
                             f'DATABASE={dbname};'
                             f'Trusted_Connection=yes;')
        return connection_string
