  
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