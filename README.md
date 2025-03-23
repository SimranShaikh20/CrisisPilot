import streamlit as st
import requests
import pydeck as pdk

# Page Configuration
st.set_page_config(
    page_title="CrisisPilot - Smart Relief",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Weather API Key (Use secrets in production)
WEATHER_API_KEY = st.secrets["weather_api_key"] if "weather_api_key" in st.secrets else "your_default_api_key"

# Helper Functions
def get_weather(city_name):
    """Fetch weather data for a given city."""
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(base_url)
    return response.json() if response.status_code == 200 else None


def get_coordinates(city_name):
    """Get coordinates for a given city."""
    base_url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    headers = {'User-Agent': 'SahaytaApp/1.0'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None


def generate_map(start_coords, end_coords=None):
    """Generate a map with route and location markers."""
    layers = [
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"position": [start_coords[1], start_coords[0]], "color": [46, 204, 113], "radius": 350}],
            get_position="position",
            get_color="color",
            get_radius="radius",
            pickable=True,
        )
    ]
    if end_coords:
        layers.extend([
            pdk.Layer(
                "LineLayer",
                data=[{
                    "start_lat": start_coords[0],
                    "start_lon": start_coords[1],
                    "end_lat": end_coords[0],
                    "end_lon": end_coords[1],
                }],
                get_source_position=["start_lon", "start_lat"],
                get_target_position=["end_lon", "end_lat"],
                get_color=[52, 152, 219],
                width_scale=2,
                width_min_pixels=3,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=[{"position": [end_coords[1], end_coords[0]], "color": [231, 76, 60], "radius": 350}],
                get_position="position",
                get_color="color",
                get_radius="radius",
                pickable=True,
            )
        ])
    view_state = pdk.ViewState(
        latitude=start_coords[0],
        longitude=start_coords[1],
        zoom=10,
        pitch=45,
    )
    return pdk.Deck(
        layers=layers,
        initial_view_state=view_state,
        map_style="light",
        tooltip={"text": "Location"},
    )


# Main Sections
def weather_section():
    st.subheader("📍 Weather Monitor")
    city_name = st.text_input("Enter City Name:", placeholder="e.g., New Delhi")
    if st.button("Get Weather Updates"):
        if city_name:
            weather_data = get_weather(city_name)
            if weather_data and 'main' in weather_data:
                st.success(f"Current Weather in {city_name}")
                st.write(f"**Temperature:** {weather_data['main']['temp']}°C")
                st.write(f"**Humidity:** {weather_data['main']['humidity']}%")
                st.write(f"**Conditions:** {weather_data['weather'][0]['description'].capitalize()}")
            else:
                st.error("Unable to fetch weather data. Please check the city name.")


def route_section():
    st.subheader("🟡 Emergency Route Planner")
    start_location = st.text_input("Start Location:", placeholder="e.g., Mumbai")
    destination_location = st.text_input("Destination:", placeholder="e.g., Pune")
    if st.button("Plan Emergency Route"):
        if start_location and destination_location:
            start_coords = get_coordinates(start_location)
            end_coords = get_coordinates(destination_location)
            if start_coords and end_coords:
                st.success(f"Emergency Route: {start_location} → {destination_location}")
                st.pydeck_chart(generate_map(start_coords, end_coords))
            else:
                st.error("Could not locate one or both locations. Please check the names.")


# Main App
def main():
    tab1, tab2 = st.tabs(["🌦️ Weather Monitor", "🟡 Route Planner"])
    with tab1:
        weather_section()
    with tab2:
        route_section()

if __name__ == "__main__":
    main()
