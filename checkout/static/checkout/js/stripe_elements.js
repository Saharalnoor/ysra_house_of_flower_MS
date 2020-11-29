  
/**
 *  Core logic/payment flow for this comes from Stripe documentations:
 *  https://stripe.com/docs/payments/accept-a-payment
 *  with minor modification and additions
 */

const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#495057'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

let card = elements.create('card', {hidePostalCode: true, style: style});
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function (event) {
    const errorDiv = document.getElementById('card-errors');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
      const errorDiv = document.getElementById('card-errors');
                let html = `
                    <span class="icon" role="alert">
                        <i class="fas fa-exclamation-circle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('.spinner-overlay-wrapper').fadeToggle(1200);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
    } else {
        if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
    }
  });
});