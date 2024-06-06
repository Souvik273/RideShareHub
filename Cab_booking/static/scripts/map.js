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

    // Add event listener to the form submit
    document.getElementById('form').addEventListener('submit', (e) => {
        e.preventDefault();
        calculateAndDisplayRoute();
        loadRideOptions();
        document.getElementById('map').style.width = '30%';
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

function getRandomPrice(base) {
    return (base + Math.random() * 50).toFixed(2);
}

let stripe = Stripe('your-publishable-key-here'); // Replace with your Stripe publishable key

function loadRideOptions() {
    const rides = [
        {
            type: "Ride Go",
            description: "Affordable compact rides",
            basePrice: 300,
            time: "7 mins away · 2:24 AM",
            icon: "public/images/logo.png"
        },
        {
            type: "Go Sedan",
            description: "Affordable sedans",
            basePrice: 350,
            time: "4 mins away · 2:23 AM",
            icon: "path/to/go_sedan_icon.png"
        },
        {
            type: "Premier",
            description: "Comfortable sedans, top-quality drivers",
            basePrice: 400,
            time: "4 mins away · 2:25 AM",
            icon: "path/to/premier_icon.png"
        }
    ];

    const container = document.getElementById("ride-selection");
    container.innerHTML = "";

    rides.forEach(ride => {
        const randomPrice = getRandomPrice(ride.basePrice);
        const oldPrice = (ride.basePrice + 40).toFixed(2);

        const rideDiv = document.createElement("div");
        rideDiv.className = "ride-option";

        rideDiv.innerHTML = `
            <img src="${ride.icon}" alt="${ride.type}">
            <div class="ride-info">
                <div class="ride-title">${ride.type}</div>
                <div class="ride-details">${ride.time}</div>
                <div class="ride-details">${ride.description}</div>
                <div class="ride-price">
                    <span class="ride-discount">25% off</span> ₹${randomPrice}
                    <span class="old-price">₹${oldPrice}</span>
                </div>
            </div>
            <button class="select-ride-button" style="display: none;">Select Ride</button>
        `;

        // Add click event listener to each ride option
        rideDiv.addEventListener('click', () => {
            // Remove the selected-ride class from all ride options
            document.querySelectorAll('.ride-option').forEach(option => {
                option.classList.remove('selected-ride');
                option.querySelector('.select-ride-button').style.display = 'none';
            });

            // Add the selected-ride class to the clicked ride option
            rideDiv.classList.add('selected-ride');
            rideDiv.querySelector('.select-ride-button').style.display = 'inline-block';
        });

        rideDiv.querySelector('.select-ride-button').addEventListener('click', () => {
            window.location.href = 'payment.html';
        });

        container.appendChild(rideDiv);
    });
}
