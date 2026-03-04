# 🚀 Smart Logistics Dashboard

A full-stack data analytics system that integrates:

- 🗄️ **MySQL Database**
- 🐍 **Python Backend**
- 📊 **Streamlit Frontend**
- 📈 **Plotly Interactive Visualizations**

It mimics enterprise logistics platforms used in supply chain operations and transportation analytics.

## 🎯 Key Objectives

- Track and analyze shipment data
- Monitor operational KPIs
- Evaluate courier performance
- Analyze delivery efficiency
- Identify cost drivers
- Detect high-cancellation routes
- Provide actionable logistics insights

## 🏗️ System Architecture

```
MySQL Database
    ↓
SQL Query Layer (queries.py)
    ↓
Database Connector (db.py)
    ↓
Streamlit Dashboard (app.py)
    ↓
Interactive Visualizations (Plotly)
```

## 🗂️ Project Structure

```
smart_logistics_project/
├── app.py              # Main Streamlit dashboard
├── queries.py          # Reusable SQL query layer
├── db.py               # Database connection module
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🛢️ Database Design

### Main Tables

- `shipments`
- `routes`
- `courier_staff`
- `costs`
- `warehouses`

### Relationships

- `shipments` → `routes` (origin + destination)
- `shipments` → `courier_staff` (courier_id)
- `shipments` → `costs` (shipment_id)
- `shipments` → `warehouses` (origin city)

The schema is designed to support analytical joins and KPI computation.

## 📊 Dashboard Features

### 1️⃣ Shipment Search & Filtering

Users can dynamically filter shipments by:

- Status (Delivered, Cancelled, In Transit)
- Origin
- Destination
- Courier ID
- Date Range

✔️ Uses parameterized SQL queries (safe & secure)  
✔️ Prevents SQL injection  
✔️ Dynamic query builder

### 2️⃣ Operational KPIs

Displays real-time logistics performance indicators:

- Total Shipments
- Delivered Percentage
- Cancelled Percentage
- Average Delivery Time
- Total Operational Cost

### 3️⃣ Delivery Performance Insights

- Average delivery time per route
- Delivery time vs distance comparison
- Identification of delayed routes

**Key Question:** Which routes are underperforming relative to distance?

### 4️⃣ Courier Performance

- Shipments handled per courier
- Delivery success rate
- Rating vs performance analysis

**Key Question:** Are high-rated couriers delivering faster?

### 5️⃣ Cost Analytics

- Total cost per shipment
- Cost distribution
- Fuel vs labor contribution
- High-cost shipment identification

**Key Question:** Is cost proportional to weight or distance?

### 6️⃣ Cancellation Analysis

- Cancellation rate by origin
- Identify high-risk cities
- Operational bottleneck detection

**Key Question:** Which cities generate maximum cancellations?

### 7️⃣ Warehouse Insights

- Warehouse capacity comparison
- High-traffic warehouse cities
- Shipment volume by origin

Helps optimize warehouse resource allocation.

## 💡 Business Insights Enabled

This system helps management answer:

- Which routes have the highest delays?
- Which couriers handle most shipments?
- Are high-rated couriers more efficient?
- Which shipments are most expensive?
- Is fuel the dominant cost driver?
- Which cities have abnormal cancellation rates?
- Are long-distance routes optimized?

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/smart-logistics-dashboard.git
cd smart-logistics-dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Setup MySQL Database

Create database:

```sql
CREATE DATABASE smart_logistics;
```

Update `db.py` with your MySQL credentials:

```python
host="localhost"
user="root"
password="your_password"
database="smart_logistics"
```

### 4️⃣ Run Application

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 🧠 Technical Highlights

✔️ Modular architecture  
✔️ Clean separation of concerns  
✔️ Reusable SQL layer  
✔️ Parameterized queries (secure)  
✔️ Scalable structure  
✔️ Optimized for large datasets (70,000+ rows)  
✔️ Interactive Plotly visualizations

## 📈 Performance Considerations

- SQL aggregation instead of Python aggregation
- Limited high-cost queries to top 200 rows
- Efficient joins using indexed keys
- Safe dynamic query builder for filtering

## 🔐 Security Practices

- Parameterized queries prevent SQL injection
- Database credentials isolated in `db.py`
- Query logic separated from UI layer

## 🏢 Real-World Use Case

This platform simulates enterprise logistics dashboards used in:

- E-commerce fulfillment centers
- Courier & parcel services
- Supply chain optimization
- Transportation analytics systems

## 🛠️ Future Enhancements

- 🔄 Real-time shipment tracking via API
- 📊 Predictive delivery delay model (Machine Learning)
- 📦 Inventory management integration
- 🔐 User authentication & role-based access
- ☁️ Cloud deployment (AWS / GCP / Azure)
- 📱 Mobile-responsive dashboard

## 🧑‍💻 Author

Ravikumar
Data Analytics / Data Engineering Project

