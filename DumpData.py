import pandas as pd
import sqlite3 
from sqlalchemy import create_engine

def get_connection():
    return create_engine("mysql+mysqlconnector://root:root@localhost:3306/smart_logistics")


# Load data
cost_df = pd.read_csv("costs.csv")
courier_staff_df = pd.read_csv("courier_staff.csv")
routes_df = pd.read_csv("routes.csv")
shipment_tracking_df = pd.read_csv("shipment_tracking.csv")
shipments_df = pd.read_json("shipments.json")
warehouses_df = pd.read_json("warehouses.json")
print(cost_df.head())
# Connect to SQLite
conn = get_connection()

# Load DataFrames into SQL tables
cost_df.to_sql("costs", conn, if_exists="replace", index=False)
shipments_df.to_sql("shipments", conn, if_exists="replace", index=False)
courier_staff_df.to_sql("courier_staff", conn, if_exists="replace", index=False)
routes_df.to_sql("routes", conn, if_exists="replace", index=False)
shipment_tracking_df.to_sql("shipment_tracking", conn, if_exists="replace", index=False)
warehouses_df.to_sql("warehouses", conn, if_exists="replace", index=False)
