import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_vehicle_data(num_vehicles=150):
    vehicles = []
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad']
    statuses = ['Active', 'Idle', 'Maintenance']
    
    for i in range(num_vehicles):
        vehicle = {
            'id': f'TRUCK{i+1:03d}',
            'driver': f'Driver {i+1}',
            'status': np.random.choice(statuses, p=[0.7, 0.2, 0.1]),
            'current_city': np.random.choice(cities),
            'speed': np.random.randint(0, 100),
            'fuel_level': np.random.randint(20, 100),
            'last_maintenance': datetime.now() - timedelta(days=np.random.randint(0, 30)),
            'next_maintenance': datetime.now() + timedelta(days=np.random.randint(1, 60)),
            'latitude': np.random.uniform(8.0, 37.0),
            'longitude': np.random.uniform(68.0, 97.0)
        }
        vehicles.append(vehicle)
    
    return pd.DataFrame(vehicles)

def generate_fuel_data(days=30):
    dates = pd.date_range(end=datetime.now(), periods=days)
    fuel_data = {
        'date': dates,
        'consumption': np.random.randint(100, 500, size=days),
        'cost': np.random.randint(5000, 25000, size=days)
    }
    return pd.DataFrame(fuel_data)

def generate_maintenance_data():
    maintenance_types = ['Oil Change', 'Tire Replacement', 'Brake Check', 'Engine Service']
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), 
                         end=datetime.now() + timedelta(days=30),
                         periods=20)
    
    maintenance = {
        'date': dates,
        'vehicle_id': [f'TRUCK{i:03d}' for i in np.random.randint(1, 151, size=20)],
        'type': np.random.choice(maintenance_types, size=20),
        'status': np.random.choice(['Completed', 'Scheduled', 'Overdue'], size=20)
    }
    return pd.DataFrame(maintenance) 