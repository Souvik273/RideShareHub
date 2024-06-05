document.getElementById('payment-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const cardNumber = document.getElementById('card-number').value;
    const expiryDate = document.getElementById('expiry-date').value;
    const cvv = document.getElementById('cvv').value;

    // Simple form validation (you can add more sophisticated validation here)
    if (!cardNumber || !expiryDate || !cvv) {
        alert('Please fill in all fields');
        return;
    }

    // Simulate payment processing
    alert('Payment Successful!\nThank you for your payment.');

    // Redirect to a success or confirmation page (if you have one)
    window.location.href = 'confirmation.html'; // Change this to your actual confirmation page
});
