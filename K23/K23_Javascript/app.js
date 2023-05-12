// Default map options
let mapOptions = {
    center: [0.0, 0.0], // Am Judensand 12, 55122 Mainz, Germany
    zoom: 2
};

// Create leaflet map object
let map = new L.map('map', mapOptions);

// Default marker options
let options = {
    iconSize: [27, 27],
    iconShape: 'marker',
    borderWidth: 2,
    borderColor: "#FFFFFF",
    textColor: "#FFFFFF",
    title: "",
    backgroundColor: "#0a84ff",
    isAlphaNumericIcon: true,
    innerIconAnchor: [0, 3]
};

// Global variable for the ISS poition
let position = null;

// Fetch position data from the API
async function getData() {
    let response = null;
    try {
        response = await fetch("http://api.open-notify.org/iss-now.json")
    } catch (error) {
        console.log(error)
        return
    };
    let data = await response.json();
    position = new L.LatLng(data.iss_position.latitude, data.iss_position.longitude);
};

// Create a marker on the map
async function createMarker() {
    await getData();
    let marker = L.marker(position, options);
    marker.options.title = `longitude: ${position.lng}, latitude: ${position.lat}`;
    map.addLayer(marker);
};

// Initialize the map and add the layer control
function loadMapFunctions() {
    // Min zoom to prevent the user from seeing the recursive background tiles
    map.options.minZoom = 2;
    // Create two layer objects, a regular map, and a map with sattelite images
    let sattelite = L.tileLayer.provider('Esri.WorldImagery');
    let base = L.tileLayer.provider('CartoDB.Positron').addTo(map);
    let baseMaps = {
        "Karte": base,
        "Satellit": sattelite
    };
    // Register the layer control on the leaflet map to switch between different layers 
    L.control.layers(baseMaps, null, { position: 'topleft' }).addTo(map);
};

document.addEventListener("DOMContentLoaded", () => {
    loadMapFunctions();
    createMarker();
});