# db_conn_util.py
import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            connection_string = DBPropertyUtil.get_property_string()
            DBConnection.connection = pyodbc.connect(connection_string)
        return DBConnection.connection
