document.addEventListener('DOMContentLoaded', (event) => {
    const navItems = document.querySelectorAll('nav a');
    const scrollTopBtn = document.getElementById('scrollTopBtn');

    function removeActiveClasses() {
        navItems.forEach(item => {
            item.classList.remove('active');
        });
    }

    function addActiveClass(link) {
        removeActiveClasses();
        link.classList.add('active');
    }

    // Add click event listener to each nav item
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            addActiveClass(item);
        });
    });

    // Function to handle intersection changes
    const handleIntersection = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                const navLink = document.querySelector(`nav a[href="#${id}"]`);
                addActiveClass(navLink);
            }
        });
    };

    // Create an Intersection Observer
    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.6 // Adjust the threshold as needed
    };

    const observer = new IntersectionObserver(handleIntersection, options);

    // Observe each section
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });

    // Initial check to set the active class based on current scroll position
    window.dispatchEvent(new Event('scroll'));

    // Scroll to top button functionality
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) { // Show button after scrolling 300px
            scrollTopBtn.style.display = "flex";
        } else {
            scrollTopBtn.style.display = "none";
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.querySelector(".sign-up");
    button.addEventListener('click', () => {
        window.location.href = "../Log-In/login.html"; 
    });
});

document.getElementById('book-cab').addEventListener('click', function() {
    // Make an AJAX request to the server to trigger the '/map' route
    fetch('/map')
        .then(response => {
            // Check if the response status is OK
            if (response.ok) {
                // If successful, redirect the user to the map page
                window.location.href = '/map';
            } else {
                // If there's an error, handle it accordingly
                console.error('Error fetching /map:', response.status);
            }
        })
        .catch(error => {
            // Handle any network errors
            console.error('Network error while fetching /map:', error);
        });
});

