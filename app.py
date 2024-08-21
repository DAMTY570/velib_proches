from flask import Flask, request, jsonify, render_template
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.distance import geodesic

app = Flask(__name__, template_folder='/Users/Abraham/Downloads/velib_proches/templates')

def get_velib_data():
    api_url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=100'
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            return data['results']  # Nous extrayons directement la liste des stations ici
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def get_closest_velib_stations(user_location, num_stations=5):
    stations = get_velib_data()
    
    if stations is None:
        return {'error': 'Failed to fetch Velib data'}
    
    user_lat = user_location['lat']
    user_lon = user_location['lon']
    
    # Calculer les distances entre l'utilisateur et chaque station
    distances = []
    for station in stations:
        station_lat = station['coordonnees_geo']['lat']
        station_lon = station['coordonnees_geo']['lon']
        station_location = (station_lat, station_lon)
        distance = geodesic((user_lat, user_lon), station_location).meters
        distances.append((station, distance))
    
    # Trier les stations par distance et sélectionner les plus proches
    sorted_stations = sorted(distances, key=lambda x: x[1])
    closest_stations = sorted_stations[:num_stations]
    
    # Préparer les résultats pour l'affichage
    result = []
    for station, distance in closest_stations:
        station_info = {
            'name': station['name'],
            'distance_meters': distance,
            'num_bikes_available': station['numbikesavailable'],
            'capacity': station['capacity'],
            'lat': station['coordonnees_geo']['lat'],
            'lon': station['coordonnees_geo']['lon']
        }
        result.append(station_info)
    
    return result


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/closest_velib_stations', methods=['POST'])
def closest_velib_stations():
    try:
        user_location = request.form.get('location')
        if user_location:
            geolocator = Nominatim(user_agent="Mozilla/5.0 (compatible; VelibProchesApp/1.0; +https://github.com/DAMTY570/velib_proches)")
            location = geolocator.geocode(user_location)
            if location:
                user_coordinates = {'lat': location.latitude, 'lon': location.longitude}
                closest_stations = get_closest_velib_stations(user_coordinates)
                return jsonify({'closest_stations': closest_stations})
            else:
                return jsonify({'error': 'Location not found'}), 400
        else:
            return jsonify({'error': 'Invalid user location data'}), 400
    except GeocoderTimedOut:
        return jsonify({'error': 'Geocoding service timed out'}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
