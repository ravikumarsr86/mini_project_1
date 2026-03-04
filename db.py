import mysql.connector
import pandas as pd

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_logistics"
    )

def run_query(query, params=None):
    conn = create_connection()
    df = pd.read_sql(query, conn, params=params)
    conn.close()
    return df