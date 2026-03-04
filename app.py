import streamlit as st
import plotly.express as px
import queries as q
from db import run_query

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Smart Logistics Dashboard", layout="wide")
st.title("🚚 Smart Logistics Management & Analytics Platform")

menu = st.sidebar.selectbox("Navigation", [
    "📊 Overview KPIs",
    "🔎 Shipment Search & Filtering",
    "📈 Delivery Performance",
    "🚚 Courier Performance",
    "💰 Cost Analytics",
    "❌ Cancellation Analysis",
    "🏭 Warehouse Insights"
])

# =========================================================
# OVERVIEW KPIs
# =========================================================
if menu == "📊 Overview KPIs":

    total = run_query(q.total_shipments())["total"][0]
    delivered = run_query(q.delivered_percentage())["delivered_pct"][0]
    cancelled = run_query(q.cancelled_percentage())["cancelled_pct"][0]
    avg_days = run_query(q.avg_delivery_time())["avg_days"][0]
    total_cost = run_query(q.total_operational_cost())["total_cost"][0]

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Shipments", total)
    col2.metric("Delivered %", f"{delivered}%")
    col3.metric("Cancelled %", f"{cancelled}%")
    col4.metric("Avg Delivery Days", avg_days)
    col5.metric("Total Operational Cost", f"${total_cost:,}")

# =========================================================
# SHIPMENT FILTER
# =========================================================
elif menu == "🔎 Shipment Search & Filtering":

    status = st.multiselect("Select Status", ["Delivered", "In Transit", "Cancelled"])
    origin = st.text_input("Origin")
    destination = st.text_input("Destination")
    courier = st.text_input("Courier ID")
    date_range = st.date_input("Order Date Range", [])

    query, params = q.build_shipment_filter_query(
        status, origin, destination, courier, date_range
    )

    df = run_query(query, params)
    st.dataframe(df)

# =========================================================
# DELIVERY PERFORMANCE
# =========================================================
elif menu == "📈 Delivery Performance":

    df = run_query(q.delivery_performance())

    st.subheader("Average Delivery Time per Route")
    st.dataframe(df)

    fig = px.scatter(df,
                     x="distance_km",
                     y="avg_days",
                     size="avg_days",
                     title="Delivery Time vs Distance")
    st.plotly_chart(fig)

# =========================================================
# COURIER PERFORMANCE
# =========================================================
elif menu == "🚚 Courier Performance":

    df = run_query(q.courier_performance())
    st.dataframe(df)

    fig = px.bar(df, x="name", y="total_shipments",
                 title="Shipments Handled per Courier")
    st.plotly_chart(fig)

    fig2 = px.scatter(df,
                      x="rating",
                      y="success_rate",
                      size="total_shipments",
                      title="Rating vs Success Rate")
    st.plotly_chart(fig2)

# =========================================================
# COST ANALYTICS
# =========================================================
elif menu == "💰 Cost Analytics":

    df = run_query(q.cost_analytics())
    st.dataframe(df)

    fig = px.histogram(df, x="total_cost", nbins=30,
                       title="Cost Distribution")
    st.plotly_chart(fig)

    fuel_pct = (df["fuel_cost"].sum() / df["total_cost"].sum()) * 100
    labor_pct = (df["labor_cost"].sum() / df["total_cost"].sum()) * 100

    pie = px.pie(values=[fuel_pct, labor_pct],
                 names=["Fuel %", "Labor %"],
                 title="Fuel vs Labor Contribution")
    st.plotly_chart(pie)

# =========================================================
# CANCELLATION
# =========================================================
elif menu == "❌ Cancellation Analysis":

    df = run_query(q.cancellation_by_origin())
    st.dataframe(df)

    fig = px.bar(df, x="origin", y="cancel_rate",
                 title="Cancellation Rate by Origin")
    st.plotly_chart(fig)

# =========================================================
# WAREHOUSE INSIGHTS
# =========================================================
elif menu == "🏭 Warehouse Insights":

    df = run_query(q.warehouse_capacity())
    st.dataframe(df)

    fig = px.bar(df, x="city", y="capacity",
                 title="Warehouse Capacity")
    st.plotly_chart(fig)

    traffic_df = run_query(q.high_traffic_cities())
    st.dataframe(traffic_df)

    fig2 = px.bar(traffic_df, x="city", y="shipment_count",
                  title="High Traffic Cities")
    st.plotly_chart(fig2)