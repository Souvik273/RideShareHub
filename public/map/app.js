// app.js

let map;
let directionsService;
let directionsRenderer;

function initMap() {
    // Initialize the map
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8
    });

    // Initialize the directions service and renderer
    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    // Add autocomplete to the input fields
    const pickupInput = document.getElementById('pickup');
    const dropInput = document.getElementById('drop');
    new google.maps.places.Autocomplete(pickupInput);
    new google.maps.places.Autocomplete(dropInput);

    // Add event listener to the button
    document.getElementById('find-route').addEventListener('click', () => {
        calculateAndDisplayRoute();
    });
}

function calculateAndDisplayRoute() {
    const pickup = document.getElementById('pickup').value;
    const drop = document.getElementById('drop').value;

    directionsService.route({
        origin: pickup,
        destination: drop,
        travelMode: google.maps.TravelMode.DRIVING
    }, (response, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
            directionsRenderer.setDirections(response);
        } else {
            window.alert('Directions request failed due to ' + status);
        }
    });
}

// Initialize the map when the window loads
window.onload = initMap;
