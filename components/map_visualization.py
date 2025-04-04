import folium
from folium import plugins
import pandas as pd
from data.demo_data import generate_vehicle_data

def create_fleet_map():
    # Generate demo data
    vehicles_df = generate_vehicle_data()
    
    # Create base map
    m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
    
    # Add vehicle markers
    for _, vehicle in vehicles_df.iterrows():
        # Customize marker color based on status
        if vehicle['status'] == 'Active':
            color = 'green'
        elif vehicle['status'] == 'Idle':
            color = 'blue'
        else:
            color = 'red'
            
        # Create popup content
        popup_content = f"""
        <b>Vehicle ID:</b> {vehicle['id']}<br>
        <b>Driver:</b> {vehicle['driver']}<br>
        <b>Status:</b> {vehicle['status']}<br>
        <b>Speed:</b> {vehicle['speed']} km/h<br>
        <b>Fuel Level:</b> {vehicle['fuel_level']}%<br>
        <b>Location:</b> {vehicle['current_city']}
        """
        
        # Add marker
        folium.Marker(
            location=[vehicle['latitude'], vehicle['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=color, icon='truck', prefix='fa'),
            tooltip=f"{vehicle['id']} - {vehicle['driver']}"
        ).add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    return m

def update_vehicle_positions():
    # This function would be called periodically to update vehicle positions
    # In a real application, this would fetch live data
    return generate_vehicle_data() 
