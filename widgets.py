import mysql.connector
from gui.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None