# ==============================
# KPI QUERIES
# ==============================

def total_shipments():
    return "SELECT COUNT(*) AS total FROM shipments;"

def delivered_percentage():
    return """
    SELECT ROUND(
        COUNT(CASE WHEN status='Delivered' THEN 1 END) * 100.0 / COUNT(*),2
    ) AS delivered_pct
    FROM shipments;
    """

def cancelled_percentage():
    return """
    SELECT ROUND(
        COUNT(CASE WHEN status='Cancelled' THEN 1 END) * 100.0 / COUNT(*),2
    ) AS cancelled_pct
    FROM shipments;
    """

def avg_delivery_time():
    return """
    SELECT ROUND(AVG(DATEDIFF(delivery_date, order_date)),2) AS avg_days
    FROM shipments
    WHERE status='Delivered';
    """

def total_operational_cost():
    return """
    SELECT ROUND(SUM(fuel_cost+labor_cost+misc_cost),2) AS total_cost
    FROM costs;
    """

# ==============================
# DELIVERY PERFORMANCE
# ==============================

def delivery_performance():
    return """
    SELECT s.origin, s.destination,
           AVG(DATEDIFF(s.delivery_date,s.order_date)) as avg_days,
           r.distance_km
    FROM shipments s
    JOIN routes r
        ON s.origin=r.origin AND s.destination=r.destination
    WHERE s.status='Delivered'
    GROUP BY s.origin,s.destination,r.distance_km
    ORDER BY avg_days DESC;
    """

# ==============================
# COURIER PERFORMANCE
# ==============================

def courier_performance():
    return """
    SELECT c.name,
           COUNT(s.shipment_id) as total_shipments,
           ROUND(100*SUM(s.status='Delivered')/COUNT(*),2) as success_rate,
           AVG(c.rating) as rating
    FROM shipments s
    JOIN courier_staff c ON s.courier_id=c.courier_id
    GROUP BY c.name
    ORDER BY total_shipments DESC;
    """

# ==============================
# COST ANALYTICS
# ==============================

def cost_analytics():
    return """
    SELECT s.origin, s.destination,
           (c.fuel_cost+c.labor_cost+c.misc_cost) as total_cost,
           c.fuel_cost, c.labor_cost, c.misc_cost
    FROM shipments s
    JOIN costs c ON s.shipment_id=c.shipment_id
    ORDER BY total_cost DESC
    LIMIT 200;
    """

# ==============================
# CANCELLATION ANALYSIS
# ==============================

def cancellation_by_origin():
    return """
    SELECT origin,
           ROUND(100*SUM(status='Cancelled')/COUNT(*),2) as cancel_rate
    FROM shipments
    GROUP BY origin
    ORDER BY cancel_rate DESC;
    """

# ==============================
# WAREHOUSE INSIGHTS
# ==============================

def warehouse_capacity():
    return """
    SELECT city, capacity
    FROM warehouses
    ORDER BY capacity DESC;
    """

def high_traffic_cities():
    return """
    SELECT origin as city, COUNT(*) as shipment_count
    FROM shipments
    GROUP BY origin
    ORDER BY shipment_count DESC;
    """

# ==============================
# DYNAMIC SHIPMENT FILTER QUERY
# ==============================

def build_shipment_filter_query(status, origin, destination, courier, date_range):

    query = "SELECT * FROM shipments WHERE 1=1"
    params = []

    if status:
        placeholders = ", ".join(["%s"] * len(status))
        query += f" AND status IN ({placeholders})"
        params.extend(status)

    if origin:
        query += " AND origin LIKE %s"
        params.append(f"%{origin}%")

    if destination:
        query += " AND destination LIKE %s"
        params.append(f"%{destination}%")

    if courier:
        query += " AND courier_id = %s"
        params.append(courier)

    if len(date_range) == 2:
        query += " AND order_date BETWEEN %s AND %s"
        params.append(str(date_range[0]))
        params.append(str(date_range[1]))

    return query, params