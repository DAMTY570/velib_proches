# Velib Closest Stations Finder

## Description

This project is a Flask web application that allows users to find the nearest Velib bike stations in real-time. It uses data from the Velib API to fetch the availability of bikes and then computes the closest stations to the user's location using geographic coordinates. 

## Features

- Fetches real-time Velib bike station data from Paris's OpenData API.
- Uses the **Geopy** library to calculate distances between the user's location and Velib stations.
- Displays the closest Velib stations with the number of available bikes and the station's capacity.

## Technologies

- **Flask**: A lightweight web framework for Python.
- **Geopy**: Python library used to locate and calculate geographic distances.
- **Requests**: A library to handle HTTP requests and fetch data from the Velib API.
- **Nominatim**: A geolocation service to convert user input (address) into latitude and longitude.
- **HTML/CSS**: Used for rendering the front-end (with a template located in `/Users/Abraham/Downloads/velib_proches/templates`).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DAMTY570/velib_proches.git
   cd velib_proches
   ```

2. **Install dependencies**:
   Use `pip` or `pipenv` to install the necessary Python packages.
   ```bash
   pip install Flask requests geopy
   ```

3. **Run the application**:
   Run the Flask app locally.
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## API Endpoints

### `/`
- **Method**: `GET`
- **Description**: Renders the homepage.

### `/closest_velib_stations`
- **Method**: `POST`
- **Parameters**: 
  - `location` (string): The user-provided address or location.
- **Description**: Takes the user’s location, geocodes it into latitude and longitude, and returns the closest Velib stations with available bikes.

## Example Usage

1. Navigate to the homepage.
2. Enter an address or location.
3. The application will return the 5 closest Velib stations with their details (station name, distance from the user, number of bikes available, and total capacity).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Abraham Krah** - [DAMTY570](https://github.com/DAMTY570)
