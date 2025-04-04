import plotly.express as px
import plotly.graph_objects as go
from data.demo_data import generate_fuel_data, generate_maintenance_data

def create_fuel_usage_chart():
    fuel_df = generate_fuel_data()
    
    fig = go.Figure()
    
    # Add consumption line
    fig.add_trace(go.Scatter(
        x=fuel_df['date'],
        y=fuel_df['consumption'],
        name='Fuel Consumption',
        line=dict(color='#1E88E5', width=2)
    ))
    
    # Add cost bar
    fig.add_trace(go.Bar(
        x=fuel_df['date'],
        y=fuel_df['cost'],
        name='Fuel Cost',
        yaxis='y2',
        marker_color='#FFA726'
    ))
    
    fig.update_layout(
        title='Fuel Usage and Cost',
        xaxis_title='Date',
        yaxis_title='Consumption (L)',
        yaxis2=dict(
            title='Cost (₹)',
            overlaying='y',
            side='right'
        ),
        template='plotly-dark',
        showlegend=True,
        height=400
    )
    
    return fig

def create_maintenance_timeline():
    maintenance_df = generate_maintenance_data()
    
    # Create Gantt chart
    fig = px.timeline(
        maintenance_df,
        x_start="date",
        x_end="date",
        y="vehicle_id",
        color="type",
        title="Maintenance Schedule",
        template="plotly-dark"
    )
    
    fig.update_layout(
        height=400,
        showlegend=True,
        xaxis_title="Date",
        yaxis_title="Vehicle ID"
    )
    
    return fig

def create_vehicle_status_chart():
    vehicles_df = generate_vehicle_data()
    status_counts = vehicles_df['status'].value_counts()
    
    fig = go.Figure(data=[go.Pie(
        labels=status_counts.index,
        values=status_counts.values,
        hole=.3,
        marker_colors=['#4CAF50', '#2196F3', '#F44336']
    )])
    
    fig.update_layout(
        title='Vehicle Status Distribution',
        template='plotly-dark',
        height=300
    )
    
    return fig 