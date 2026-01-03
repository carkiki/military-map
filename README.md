# US Military Bases Map & Navigation System

An interactive web application built with Python Flask that displays US military bases on an interactive map and provides navigation routing that avoids military exclusion zones.

## Features

- **Interactive Map**: View all major US military installations on an interactive map
- **Base Information**: Click on any base to see detailed information including:
  - Base name and military branch
  - State location
  - Description of the facility
  - Exact coordinates
- **Exclusion Zones**: Visual representation of 10km exclusion zones around each base
- **Navigation Planning**: Calculate routes between two points that avoid military exclusion zones
- **Point Checker**: Verify if specific coordinates fall within any exclusion zone
- **Color-Coded Markers**: Different colors for each military branch:
  - Green: Army
  - Blue: Navy
  - Light Blue: Air Force
  - Red: Marine Corps
  - Purple: Space Force
  - Orange: Joint Bases

## Technology Stack

- **Backend**: Python Flask
- **Mapping**: Folium & Leaflet.js
- **Geospatial**: GeoPy for distance calculations
- **Frontend**: HTML5, CSS3, JavaScript

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download this repository**

2. **Navigate to the project directory**
   ```bash
   cd military-map
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Application

1. **Run the Flask application**
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **The application will start** and you'll see the message:
   ```
   Starting Military Bases Map Application...
   Open your browser and navigate to: http://localhost:5000
   Press CTRL+C to stop the server
   ```

### Using the Application

#### Viewing Military Bases

- The map loads with all major US military bases displayed
- Each base has a colored marker based on its military branch
- A semi-transparent circle shows the 10km exclusion zone around each base
- Click any marker to view detailed information about that base

#### Planning Navigation Routes

1. **Set Start Point**:
   - Either enter coordinates manually in the "Start Point" fields
   - Or click "Click Map to Set" and click anywhere on the map

2. **Set End Point**:
   - Either enter coordinates manually in the "End Point" fields
   - Or click "Click Map to Set" and click anywhere on the map

3. **Calculate Route**:
   - Click "Calculate Safe Route"
   - The application will draw a blue line showing the recommended path
   - The route automatically avoids military exclusion zones
   - View route details including:
     - Total distance in kilometers
     - Number of waypoints
     - Any warnings if start/end points are in exclusion zones

4. **Clear Route**:
   - Click "Clear Route" to remove the route and markers

#### Checking Specific Points

1. Enter latitude and longitude coordinates in the "Point Checker" section
2. Click "Check Point"
3. The application will indicate if the point is within any exclusion zone
4. A temporary marker will appear on the map showing the checked location

## API Endpoints

The application provides several API endpoints:

### GET `/api/bases`
Returns JSON array of all military bases with their information

### GET `/api/map`
Returns the Folium map as HTML

### POST `/api/route`
Calculate route avoiding exclusion zones

**Request body:**
```json
{
  "start_lat": 34.0522,
  "start_lon": -118.2437,
  "end_lat": 40.7128,
  "end_lon": -74.0060
}
```

**Response:**
```json
{
  "waypoints": [[lat, lon], ...],
  "total_distance_km": 450.23,
  "warnings": [],
  "exclusion_radius_km": 10
}
```

### POST `/api/check_point`
Check if a point is in an exclusion zone

**Request body:**
```json
{
  "lat": 35.1390,
  "lon": -79.0060
}
```

**Response:**
```json
{
  "in_exclusion_zone": true,
  "base_name": "Fort Liberty",
  "exclusion_radius_km": 10
}
```

## Project Structure

```
military-map/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── data/
│   └── military_bases.json    # Military base data
│
├── templates/
│   └── index.html             # Main HTML template
│
└── static/
    └── style.css              # CSS styling
```

## Data Source

All military base information displayed in this application is publicly available data. The locations and basic information about US military installations are not classified and can be found through various public sources.

## Exclusion Zones

The 10km exclusion zones are illustrative and used for navigation planning purposes. These zones help users plan routes that maintain appropriate distance from military installations.

## Customization

### Changing Exclusion Radius

Edit the `EXCLUSION_RADIUS_KM` variable in `app.py`:

```python
EXCLUSION_RADIUS_KM = 15  # Change to desired radius in kilometers
```

### Adding More Bases

Edit `data/military_bases.json` and add new entries following this format:

```json
{
  "name": "Base Name",
  "branch": "Military Branch",
  "lat": 0.0000,
  "lon": 0.0000,
  "state": "State Name",
  "description": "Description of the base"
}
```

### Changing Map Style

The application uses OpenStreetMap tiles by default. You can change the tile provider in `templates/index.html` by modifying the tile layer URL.

## Troubleshooting

### Port 5000 Already in Use

If port 5000 is already in use, you can change it in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change port number
```

### Dependencies Installation Issues

If you encounter issues installing dependencies, try:

```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### Map Not Loading

- Check your internet connection (required for map tiles)
- Ensure JavaScript is enabled in your browser
- Check browser console for any errors

## Security & Privacy

- This application runs locally on your machine (localhost)
- No data is sent to external servers except for map tiles from OpenStreetMap
- All routing calculations are performed locally

## Contributing

This project displays public information about US military installations. If you have updates to base information or want to add more bases, please ensure all information is from public sources.

## License

This project is for educational and informational purposes. All military base data is publicly available information.

## Disclaimer

The information provided in this application is for navigation planning purposes only. Always follow local laws, regulations, and posted restrictions when traveling near or around military installations. The exclusion zones shown are illustrative and do not represent official restricted areas.
