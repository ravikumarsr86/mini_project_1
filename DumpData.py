import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    return create_engine("mysql+mysqlconnector://root:root@localhost:3306/smart_logistics")


# Load data
cost_df = pd.read_csv("./resources/costs.csv")
courier_staff_df = pd.read_csv("c./resources/courier_staff.csv")
routes_df = pd.read_csv("./resources/routes.csv")
shipment_tracking_df = pd.read_csv("./resources/shipment_tracking.csv")
shipments_df = pd.read_json("./resources/shipments.json")
warehouses_df = pd.read_json("./resources/warehouses.json")

# Connect to SQLite
conn = get_connection()

# Load DataFrames into SQL tables
cost_df.to_sql("costs", conn, if_exists="replace", index=False)
shipments_df.to_sql("shipments", conn, if_exists="replace", index=False)
courier_staff_df.to_sql("courier_staff", conn, if_exists="replace", index=False)
routes_df.to_sql("routes", conn, if_exists="replace", index=False)
shipment_tracking_df.to_sql("shipment_tracking", conn, if_exists="replace", index=False)
warehouses_df.to_sql("warehouses", conn, if_exists="replace", index=False)
