"""
Military Bases Map Application
A Flask web application for visualizing US military bases and providing navigation that avoids them.
"""

from flask import Flask, render_template, jsonify, request
import folium
from folium import plugins
import json
import math
from geopy.distance import geodesic

app = Flask(__name__)

# Load military bases data
def load_military_bases():
    """Load military bases from JSON file"""
    with open('data/military_bases.json', 'r') as f:
        return json.load(f)

# Calculate exclusion zone radius (in km) - using 10km as default safety buffer
EXCLUSION_RADIUS_KM = 10

def is_point_in_exclusion_zone(lat, lon, bases, radius_km=EXCLUSION_RADIUS_KM):
    """Check if a point is within exclusion zone of any military base"""
    point = (lat, lon)
    for base in bases:
        base_point = (base['lat'], base['lon'])
        distance = geodesic(point, base_point).kilometers
        if distance <= radius_km:
            return True, base['name']
    return False, None

def create_waypoints_avoiding_bases(start_lat, start_lon, end_lat, end_lon, bases):
    """
    Create navigation waypoints that avoid military bases
    Uses a simple straight-line path with detours around exclusion zones
    """
    waypoints = [(start_lat, start_lon)]

    # Simple pathfinding: check if direct route passes through exclusion zones
    # If it does, add waypoints to go around them
    num_segments = 20
    current_lat, current_lon = start_lat, start_lon

    for i in range(1, num_segments + 1):
        # Calculate intermediate point
        ratio = i / num_segments
        inter_lat = start_lat + (end_lat - start_lat) * ratio
        inter_lon = start_lon + (end_lon - start_lon) * ratio

        # Check if this point is in an exclusion zone
        in_zone, base_name = is_point_in_exclusion_zone(inter_lat, inter_lon, bases)

        if in_zone:
            # Find the problematic base and route around it
            for base in bases:
                base_point = (base['lat'], base['lon'])
                test_point = (inter_lat, inter_lon)
                if geodesic(test_point, base_point).kilometers <= EXCLUSION_RADIUS_KM:
                    # Calculate perpendicular offset to go around
                    # Simple approach: offset by 15km perpendicular to direct path
                    angle = math.atan2(end_lon - start_lon, end_lat - start_lat)
                    perp_angle = angle + math.pi / 2

                    offset_km = 15
                    offset_lat = offset_km / 111  # roughly 111km per degree latitude
                    offset_lon = offset_km / (111 * math.cos(math.radians(inter_lat)))

                    detour_lat = inter_lat + offset_lat * math.cos(perp_angle)
                    detour_lon = inter_lon + offset_lon * math.sin(perp_angle)

                    waypoints.append((detour_lat, detour_lon))
                    break
        else:
            if len(waypoints) == 1 or geodesic(waypoints[-1], (inter_lat, inter_lon)).kilometers > 50:
                waypoints.append((inter_lat, inter_lon))

    waypoints.append((end_lat, end_lon))
    return waypoints

@app.route('/')
def index():
    """Render the main map page"""
    return render_template('index.html')

@app.route('/api/bases')
def get_bases():
    """API endpoint to get all military bases"""
    bases = load_military_bases()
    return jsonify(bases)

@app.route('/api/map')
def get_map():
    """Generate and return the Folium map HTML"""
    bases = load_military_bases()

    # Create map centered on continental US
    m = folium.Map(
        location=[39.8283, -98.5795],  # Geographic center of continental US
        zoom_start=5,
        tiles='OpenStreetMap'
    )

    # Add different tile layers
    folium.TileLayer('CartoDB positron', name='Light Map').add_to(m)
    folium.TileLayer('CartoDB dark_matter', name='Dark Map').add_to(m)

    # Color mapping for different branches
    branch_colors = {
        'Army': 'green',
        'Navy': 'blue',
        'Air Force': 'lightblue',
        'Marine Corps': 'red',
        'Space Force': 'purple',
        'Joint': 'orange'
    }

    # Add markers for each military base
    for base in bases:
        color = branch_colors.get(base['branch'], 'gray')

        # Create popup content
        popup_html = f"""
        <div style="width: 250px;">
            <h4>{base['name']}</h4>
            <p><strong>Branch:</strong> {base['branch']}</p>
            <p><strong>State:</strong> {base['state']}</p>
            <p><strong>Description:</strong> {base['description']}</p>
            <p><strong>Coordinates:</strong> {base['lat']:.4f}, {base['lon']:.4f}</p>
        </div>
        """

        # Add marker
        folium.Marker(
            location=[base['lat'], base['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=base['name'],
            icon=folium.Icon(color=color, icon='info-sign')
        ).add_to(m)

        # Add exclusion zone circle
        folium.Circle(
            location=[base['lat'], base['lon']],
            radius=EXCLUSION_RADIUS_KM * 1000,  # Convert to meters
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.1,
            opacity=0.3,
            popup=f"Exclusion Zone: {base['name']} ({EXCLUSION_RADIUS_KM}km radius)",
            tooltip=f"Exclusion Zone: {EXCLUSION_RADIUS_KM}km"
        ).add_to(m)

    # Add layer control
    folium.LayerControl().add_to(m)

    # Add fullscreen option
    plugins.Fullscreen().add_to(m)

    # Add measure control
    plugins.MeasureControl().add_to(m)

    # Save to HTML string
    return m._repr_html_()

@app.route('/api/route', methods=['POST'])
def calculate_route():
    """Calculate route avoiding military bases"""
    data = request.json
    start_lat = float(data['start_lat'])
    start_lon = float(data['start_lon'])
    end_lat = float(data['end_lat'])
    end_lon = float(data['end_lon'])

    bases = load_military_bases()

    # Check if start or end points are in exclusion zones
    start_in_zone, start_base = is_point_in_exclusion_zone(start_lat, start_lon, bases)
    end_in_zone, end_base = is_point_in_exclusion_zone(end_lat, end_lon, bases)

    warnings = []
    if start_in_zone:
        warnings.append(f"Warning: Start point is within exclusion zone of {start_base}")
    if end_in_zone:
        warnings.append(f"Warning: End point is within exclusion zone of {end_base}")

    # Generate waypoints
    waypoints = create_waypoints_avoiding_bases(start_lat, start_lon, end_lat, end_lon, bases)

    # Calculate total distance
    total_distance = 0
    for i in range(len(waypoints) - 1):
        total_distance += geodesic(waypoints[i], waypoints[i+1]).kilometers

    return jsonify({
        'waypoints': [[lat, lon] for lat, lon in waypoints],
        'total_distance_km': round(total_distance, 2),
        'warnings': warnings,
        'exclusion_radius_km': EXCLUSION_RADIUS_KM
    })

@app.route('/api/check_point', methods=['POST'])
def check_point():
    """Check if a specific point is in an exclusion zone"""
    data = request.json
    lat = float(data['lat'])
    lon = float(data['lon'])

    bases = load_military_bases()
    in_zone, base_name = is_point_in_exclusion_zone(lat, lon, bases)

    return jsonify({
        'in_exclusion_zone': in_zone,
        'base_name': base_name,
        'exclusion_radius_km': EXCLUSION_RADIUS_KM
    })

if __name__ == '__main__':
    print("Starting Military Bases Map Application...")
    print("Open your browser and navigate to: http://localhost:5000")
    print("Press CTRL+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
