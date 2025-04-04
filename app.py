import streamlit as st
import pandas as pd
import plotly.express as px
from components.map_visualization import create_fleet_map
from components.charts import create_fuel_usage_chart, create_maintenance_timeline, create_vehicle_status_chart
from data.demo_data import generate_vehicle_data, generate_fuel_data, generate_maintenance_data

# Page config
st.set_page_config(
    page_title="Fleet Management Dashboard",
    page_icon="🚛",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
    }
    .metric-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        margin: 10px;
    }
    .stAlert {
        background-color: #1E1E1E;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Fleet Management")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Vehicles", "Drivers", "Alerts", "Settings"]
)

# Main content
if page == "Dashboard":
    st.title("Fleet Management Dashboard")
    
    # Time filter
    col1, col2, col3 = st.columns(3)
    with col1:
        time_filter = st.selectbox(
            "Time Range",
            ["Today", "This Week", "Custom Range"]
        )
    
    # Metrics
    vehicles_df = generate_vehicle_data()
    metrics = {
        'total_vehicles': len(vehicles_df),
        'active_vehicles': len(vehicles_df[vehicles_df['status'] == 'Active']),
        'idle_vehicles': len(vehicles_df[vehicles_df['status'] == 'Idle']),
        'distance_covered': vehicles_df['speed'].sum(),
        'fuel_consumption': generate_fuel_data(1)['consumption'].sum(),
        'maintenance_alerts': len(vehicles_df[vehicles_df['status'] == 'Maintenance'])
    }
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.metric("Total Vehicles", metrics['total_vehicles'])
    with col2:
        st.metric("Active Vehicles", metrics['active_vehicles'])
    with col3:
        st.metric("Idle Vehicles", metrics['idle_vehicles'])
    with col4:
        st.metric("Distance (km)", f"{metrics['distance_covered']:,.0f}")
    with col5:
        st.metric("Fuel (L)", f"{metrics['fuel_consumption']:,.0f}")
    with col6:
        st.metric("Maintenance Alerts", metrics['maintenance_alerts'])
    
    # Map and Charts
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Fleet Location")
        fleet_map = create_fleet_map()
        st.components.v1.html(fleet_map._repr_html_(), height=500)
    with col2:
        st.subheader("Vehicle Status")
        status_chart = create_vehicle_status_chart()
        st.plotly_chart(status_chart, use_container_width=True)
    
    # Fuel and Maintenance Charts
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Fuel Usage")
        fuel_chart = create_fuel_usage_chart()
        st.plotly_chart(fuel_chart, use_container_width=True)
    with col2:
        st.subheader("Maintenance Schedule")
        maintenance_chart = create_maintenance_timeline()
        st.plotly_chart(maintenance_chart, use_container_width=True)

elif page == "Vehicles":
    st.title("Vehicle Management")
    vehicles_df = generate_vehicle_data()
    st.dataframe(vehicles_df)

elif page == "Drivers":
    st.title("Driver Management")
    vehicles_df = generate_vehicle_data()
    driver_df = vehicles_df[['driver', 'vehicle_id', 'status', 'current_city']]
    st.dataframe(driver_df)

elif page == "Alerts":
    st.title("System Alerts")
    maintenance_df = generate_maintenance_data()
    alerts_df = maintenance_df[maintenance_df['status'] == 'Overdue']
    if not alerts_df.empty:
        for _, alert in alerts_df.iterrows():
            st.error(f"🚨 Maintenance overdue for {alert['vehicle_id']}: {alert['type']}")
    else:
        st.success("No active alerts")

elif page == "Settings":
    st.title("Settings")
    st.write("Dashboard settings and configuration options will appear here") 