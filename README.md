# Fleet Management Dashboard

A professional 3D fleet management dashboard built with Streamlit, featuring real-time vehicle tracking, metrics visualization, and maintenance scheduling.

## Features

- Interactive map showing vehicle locations
- Real-time metrics and KPIs
- Fuel usage and cost tracking
- Maintenance schedule management
- Vehicle and driver management
- Alert system for maintenance
- Dark theme interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fleet-dashboard.git
cd fleet-dashboard
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

To run the dashboard locally:
```bash
streamlit run app.py
```

## Deployment

This app is deployed on Streamlit Cloud. Visit the deployment at: [Your Streamlit Cloud URL]

## Project Structure

```
fleet-dashboard/
├── app.py                 # Main Streamlit application
├── components/            # Reusable components
│   ├── map_visualization.py
│   ├── charts.py
│   └── navigation.py
├── data/                 # Data generation and management
│   └── demo_data.py
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 